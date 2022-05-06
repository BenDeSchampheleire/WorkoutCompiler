class Visitor:
    """General Visitor class to be inherited from. Acts as a dummy Visitor by printing which elements are visited"""

    def visit(self, program):
        program.accept(self)
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
