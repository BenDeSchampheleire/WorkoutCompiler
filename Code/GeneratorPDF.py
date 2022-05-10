from Code.PDF import PDF
from Code.Visitor import Visitor


class GeneratorPDF(Visitor):
    """Type of Visitor that creates a pdf file of the program based on the PyPDF class. Contains the traditional methods of the Visitor Pattern: visit...(self, ...)"""

    pdf = PDF(orientation='P', unit='mm', format='A4')
    exercise_counter = 0
    workout_counter = 0

    def generatePDF(self, program, name):
        program.accept(self)
        file_name = "../" + name + '.pdf'
        GeneratorPDF.pdf.set_title("Workout Program")
        GeneratorPDF.pdf.set_author("Ben De Schampheleire")
        GeneratorPDF.pdf.output(file_name, 'F')
        return program

    def visitProgram(self, program):
        GeneratorPDF.pdf.add_page()
        GeneratorPDF.pdf.frame()
        GeneratorPDF.pdf.title(program.name.string)
        program.name.accept(self)
        for workout in program.workouts:
            if GeneratorPDF.workout_counter != 0:
                GeneratorPDF.pdf.add_page()
                GeneratorPDF.pdf.frame()
            workout.accept(self)
            GeneratorPDF.workout_counter += 1
        return program

    def visitWorkout(self, workout):
        GeneratorPDF.pdf.subtitle("Workout " + str(GeneratorPDF.workout_counter + 1) + ": " + workout.name.string)
        workout.name.accept(self)
        for exercise in workout.exercises:
            exercise.accept(self)
            GeneratorPDF.exercise_counter += 1
        GeneratorPDF.exercise_counter = 0
        return workout

    def visitExercise(self, exercise):
        GeneratorPDF.pdf.insert_exercise_name(GeneratorPDF.exercise_counter, exercise.name.string)
        image_attributes = GeneratorPDF.pdf.search_exercise_image(exercise.name.string)  # returns False when image is not found
        image_path = GeneratorPDF.pdf.get_image(image_attributes)
        GeneratorPDF.pdf.insert_exercise_image(GeneratorPDF.exercise_counter, image_path)
        GeneratorPDF.pdf.insert_exercise_specs(GeneratorPDF.exercise_counter, exercise)
        exercise.name.accept(self)
        return exercise

    def visitName(self, name):
        return name
