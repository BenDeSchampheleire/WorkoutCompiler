class Node:
    """Represents a node in the AST. Class to be inherited from. Allows metaprogramming of the method accept()"""

    def accept(self, visitor):
        """Accept the visitor using a metaprogramming approach"""

        class_name = self.__class__.__name__
        method_name = getattr(visitor, "visit" + class_name)
        method_name(self)


class Program (Node):
    """Program node, containing a Name node and several Workout nodes"""

    def __init__(self):
        self.name = None
        self.workouts = []


class Workout (Node):
    """Workout node, containing a Name node and several Exercise nodes"""

    def __init__(self):
        self.name = None
        self.exercises = []


class Exercise (Node):
    """Exercise node, containing a Name node and the specifications of the exercise: number of reps, sets and rest"""

    def __init__(self):
        self.name = None
        self.sets = None
        self.reps = None
        self.rest = None


class Name (Node):
    """Name node, contains a String with the name of a Program/Workout/Exercise"""

    def __init__(self):
        self.string = ""
