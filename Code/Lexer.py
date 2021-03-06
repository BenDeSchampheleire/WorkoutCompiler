import re
import sys

regexExpressions = [
    # Comments and whitespaces
    (r'\/\/[\s\S]*\n', 'COMMENT'),
    (r'[ \n\t]+', None),

    # Special characters
    (r'\;', 'TERMINATOR'),
    (r'\"', 'QUOTE'),
    (r'\(', 'LPARENTHESES'),
    (r'\)', 'RPARENTHESES'),
    (r'\{', 'LBRACES'),
    (r'\}', 'RBRACES'),
    (r'\,', 'COMMA'),
    (r'\-', 'MINUS'),

    # Identifiers & Integers
    (r'Program\b', 'PROGRAM'),
    (r'Workout\b', 'WORKOUT'),
    (r'Exercise\b', 'EXERCISE'),
    (r'[a-zA-Z]\w*', 'WORD'),
    (r'\d+', 'NUMBER'),
]


class Token:
    """
    tag: String
        Name of the token's type

    value: String
        Value of the token

    position: List[Int,Int]
        Tuple to point out the token's in the input file (line number, position)
    """

    def __init__(self, tag, value, position):
        self.tag = tag
        self.value = value
        self.position = position

    def __repr__(self):
        return self.value

    def __eq__(self, other):
        if isinstance(other, Token):
            return self.tag == other.tag and self.value == other.value and self.position == other.position
        return False


class Lexer:
    """
    Component in charge of the transformation of raw data to tokens.
    """

    def __init__(self):
        self.tokens = []

    def lex(self, inputText):
        """
        Main lexer function:
        Creates a token for every detected regular expression

        SEE Token for more info
        """
        # Crawl through the input file
        for lineNumber, line in enumerate(inputText):
            lineNumber += 1
            position = 0
            # Crawl through the line
            while position < len(line):
                match = None
                for tokenRegex in regexExpressions:
                    pattern, tag = tokenRegex
                    regex = re.compile(pattern)
                    match = regex.match(line, position)
                    if match:
                        data = match.group(0)
                        # This condition is needed to avoid the creation of whitespace tokens
                        if tag:
                            token = Token(tag, data, [lineNumber, position])
                            self.tokens.append(token)
                        # Renew the position
                        position = match.end(0)
                        break
                # No match detected --> Wrong syntax in the input file
                if not match:
                    print("No match detected on line and position: ({},{})".format(lineNumber, position+1))
                    print(line[position:])
                    sys.exit(1)

        return self.tokens
