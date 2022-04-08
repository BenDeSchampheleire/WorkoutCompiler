class Visitor:

    def visit(self, program):
        program.accept(self)
        print("\nVisitor: analysis successful!")
        return program

    def visitProgram(self, program):
        print("Visiting Program")
        program.name.accept(self)
        for workout in program.workouts:
            workout.accept(self)
        return program

    def visitWorkout(self, workout):
        print("Visiting Workout")
        workout.name.accept(self)
        for exercise in workout.exercises:
            exercise.accept(self)
        return workout

    def visitExercise(self, exercise):
        print("Visiting Exercise")
        exercise.name.accept(self)
        return exercise

    @staticmethod
    def visitName(name):
        print("Visiting Name")
        return name
