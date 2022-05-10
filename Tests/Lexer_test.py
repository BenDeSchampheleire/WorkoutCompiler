import unittest

from Code.Lexer import Lexer, Token


class Lexer_test(unittest.TestCase):
    """
        Test class of the Lexer.
    """

    def initialize(self):
        """
        Initialize a Lexer
        """

        lexer = Lexer()
        self.assertEqual([], lexer.tokens)

    def test_lex(self):
        """
        Test the output of the method lex.
        """

        lexer = Lexer()

        input_test = [
            'Program("First") {',
            '    Workout("Second") {',
            '        Exercise("Third", 1, 1, 1);',
            '    }',
            '}'
        ]

        target = [Token('PROGRAM', 'Program', [1, 0]),
                  Token('LPARENTHESES', '(', [1, 7]),
                  Token('QUOTE', '"', [1, 8]),
                  Token('WORD', 'First', [1, 9]),
                  Token('QUOTE', '"', [1, 14]),
                  Token('RPARENTHESES', ')', [1, 15]),
                  Token('LBRACES', '{', [1, 17]),
                  Token('WORKOUT', 'Workout', [2, 4]),
                  Token('LPARENTHESES', '(', [2, 11]),
                  Token('QUOTE', '"', [2, 12]),
                  Token('WORD', 'Second', [2, 13]),
                  Token('QUOTE', '"', [2, 19]),
                  Token('RPARENTHESES', ')', [2, 20]),
                  Token('LBRACES', '{', [2, 22]),
                  Token('EXERCISE', 'Exercise', [3, 8]),
                  Token('LPARENTHESES', '(', [3, 16]),
                  Token('QUOTE', '"', [3, 17]),
                  Token('WORD', 'Third', [3, 18]),
                  Token('QUOTE', '"', [3, 23]),
                  Token('COMMA', ',', [3, 24]),
                  Token('NUMBER', '1', [3, 26]),
                  Token('COMMA', ',', [3, 27]),
                  Token('NUMBER', '1', [3, 29]),
                  Token('COMMA', ',', [3, 30]),
                  Token('NUMBER', '1', [3, 32]),
                  Token('RPARENTHESES', ')', [3, 33]),
                  Token('TERMINATOR', ';', [3, 34]),
                  Token('RBRACES', '}', [4, 4]),
                  Token('RBRACES', '}', [5, 0])
                  ]

        lexed = lexer.lex(input_test)
        self.assertEqual(target, lexed)


if __name__ == '__main__':
    unittest.main()
