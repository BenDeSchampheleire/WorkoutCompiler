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

    def __eq__(self, other):
        if isinstance(other, Program):
            for index, workout in enumerate(self.workouts):
                if workout != other.workouts[index]:
                    return False
            if self.name == other.name:
                return True
        return False


class Workout (Node):
    """Workout node, containing a Name node and several Exercise nodes"""

    def __init__(self):
        self.name = None
        self.exercises = []

    def __eq__(self, other):
        if isinstance(other, Workout):
            for index, exercise in enumerate(self.exercises):
                if exercise != other.exercises[index]:
                    return False
            if self.name == other.name:
                return True
        return False


class Exercise (Node):
    """Exercise node, containing a Name node and the specifications of the exercise: number of reps, sets and rest"""

    def __init__(self):
        self.name = None
        self.sets = None
        self.reps = None
        self.rest = None

    def __eq__(self, other):
        if isinstance(other, Exercise):
            return self.name == other.name and self.sets == other.sets and self.reps == other.reps and self.rest == other.rest
        return False


class Name (Node):
    """Name node, contains a String with the name of a Program/Workout/Exercise"""

    def __init__(self):
        self.string = ""

    def __eq__(self, other):
        if isinstance(other, Name):
            return self.string == other.string
        return False
