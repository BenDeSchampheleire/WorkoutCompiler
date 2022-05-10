import unittest

from Code.Lexer import Token


class Token_test(unittest.TestCase):
    """
    Test class of the Tokens.
    """

    def initialize(self):
        """
        Initialize a Token
        """

        token = Token("EXERCISE", "Incline Barbell Bench Press", (1, 1))
        self.assertEqual("EXERCISE", token.tag)
        self.assertEqual("Incline Barbell Bench Press", token.value)
        self.assertEqual((1, 1), token.position)

    def test_equality(self):
        """
        Test the equality between two tokens
        """

        with self.subTest():
            self.assertEqual(Token("EXERCISE", "Token", (1, 1)),
                             Token("EXERCISE", "Token", (1, 1)), "The Tokens should be the same")
        with self.subTest():
            self.assertNotEqual(Token("WORKOUT", "Token", (1, 1)),
                                Token("EXERCISE", "Token", (1, 1)), "The tags should be different")
        with self.subTest():
            self.assertNotEqual(Token("EXERCISE", "Token1", (1, 1)),
                                Token("EXERCISE", "Token2", (1, 1)), "The values should be different")
        with self.subTest():
            self.assertNotEqual(Token("EXERCISE", "Token", (1, 1)),
                                Token("EXERCISE", "Token", (1, 2)), "The positions should be different")


if __name__ == "__main__":
    unittest.main()
