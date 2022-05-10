import unittest

from Code.AST import *
from Code.Lexer import Lexer
from Code.Parser import Parser


class Parser_test(unittest.TestCase):
    """
        Test class of the Parser.
    """

    def initialize(self):
        """
        Initialize a Lexer
        """

        parser = Parser()
        self.assertEqual([], parser.tokens)

    def test_equality(self):
        """
            Test the output of the method parse.
        """

        lexer = Lexer()
        parser = Parser()

        input_test = [
            'Program("First") {',
            '    Workout("Second") {',
            '        Exercise("Third", 1, 1, 1);',
            '    }',
            '}'
        ]

        exercise = Exercise()
        name3 = Name()
        name3.string = "Third"
        exercise.name = name3
        exercise.reps = 1
        exercise.sets = 1
        exercise.rest = 1
        workout = Workout()
        name2 = Name()
        name2.string = "Second"
        workout.name = name2
        workout.exercises.append(exercise)
        target = Program()
        name1 = Name()
        name1.string = "First"
        target.name = name1
        target.workouts.append(workout)

        ast = parser.parse(lexer.lex(input_test))
        self.assertEqual(target, ast)


if __name__ == '__main__':
    unittest.main()
