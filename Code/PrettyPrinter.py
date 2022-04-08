from Code.Visitor import Visitor


class PrettyPrinter(Visitor):

    def prettyPrint(self, program):
        print("\n ---------------------------------------------------------- \n")
        program.accept(self)
        print("\n ---------------------------------------------------------- \n")
        return program

    def visitProgram(self, program):
        print("Program: ", end='')
        program.name.accept(self)
        for workout in program.workouts:
            workout.accept(self)
        return program

    def visitWorkout(self, workout):
        print("\t Workout: ", end='')
        workout.name.accept(self)
        for exercise in workout.exercises:
            exercise.accept(self)
        return workout

    def visitExercise(self, exercise):
        print("\t \t Exercise: ", end='')
        exercise.name.accept(self)
        print("\t \t \t sets: %d, reps: %d, rest: %d" % (exercise.sets, exercise.reps, exercise.rest))
        return exercise

    def visitName(self, name):
        print(name.string)
        return name
