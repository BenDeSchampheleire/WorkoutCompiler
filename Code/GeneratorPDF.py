from Code.PDF import PDF
from Code.Visitor import Visitor


class GeneratorPDF(Visitor):
    pdf = PDF(orientation='P', unit='mm', format='A4')
    exercise_counter = 0

    def generatePDF(self, program, name):
        program.accept(self)
        file_name = name + '.pdf'
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
            workout.accept(self)
        return program

    def visitWorkout(self, workout):
        GeneratorPDF.pdf.subtitle(workout.name.string)
        workout.name.accept(self)
        for exercise in workout.exercises:
            exercise.accept(self)
            GeneratorPDF.exercise_counter += 1
        GeneratorPDF.exercise_counter = 0
        return workout

    def visitExercise(self, exercise):
        GeneratorPDF.pdf.insert_text(GeneratorPDF.exercise_counter, exercise.name.string)
        GeneratorPDF.pdf.insert_image(GeneratorPDF.exercise_counter, "Resources/Logo_SecVeh.png")
        exercise.name.accept(self)
        return exercise

    def visitName(self, name):
        return name
