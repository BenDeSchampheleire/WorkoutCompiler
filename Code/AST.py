class Node:

    def accept(self, visitor):
        class_name = self.__class__.__name__
        method_name = getattr(visitor, "visit" + class_name)
        method_name(self)


class Program (Node):

    def __init__(self):
        self.name = None
        self.workouts = []


class Workout (Node):

    def __init__(self):
        self.name = None
        self.exercises = []


class Exercise (Node):

    def __init__(self):
        self.name = None
        self.sets = None
        self.reps = None
        self.rest = None


class Name (Node):

    def __init__(self):
        self.string = ""
