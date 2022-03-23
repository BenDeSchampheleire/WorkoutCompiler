import sys

from AST import *


class Parser:

    def __init__(self):
        self.tokens = []

    # ==========================
    #      Helper Functions
    # ==========================

    def error(self, message):
        """ Error template """

        print('ERROR at {}:'.format(str(self.peek().position)), message)
        sys.exit(1)

    def peek(self, n=1):
        """ Returns the next token in the list WITHOUT popping it """

        try:
            return self.tokens[n - 1]
        except IndexError:
            self.error('No more tokens left.')

    def expect(self, tag):
        """ Pops the next token from the tokens list and tests its type through the tag """

        next_token = self.peek()
        if next_token.tag == tag:
            return self.accept()
        else:
            self.error('Expected {}, got {} instead'.format(tag, next_token.tag))

    def accept(self):
        """ Pops the token out of the tokens list and log its tag/value combination """

        # self.peek()
        return self.tokens.pop(0)

    def remove_comments(self):
        """ Removes the comments from the token list by testing their tags """

        self.tokens = [token for token in self.tokens if token.tag != "COMMENT"]

        # ==========================
        #      Parse Functions
        # ==========================

    def parse(self, tokens):
        """ Main function: launches the parsing operation given a list of tokens """

        self.tokens = tokens
        self.remove_comments()
        ast = self.parse_program()
        return ast

    def parse_program(self):
        """ Parses a Program which is a succession of Workouts """

        program = Program()
        self.expect("PROGRAM")
        self.expect("LPARENTHESES")
        self.expect("QUOTE")

        name = self.parse_name()
        program.name = name

        self.expect("QUOTE")
        self.expect("RPARENTHESES")
        self.expect("LBRACES")

        while len(self.tokens) > 0:
            workout = self.parse_workout()
            program.workouts.append(workout)

        return program

    def parse_workout(self):
        """ Parses a Workout consisting of one or multiple Exercises """

        workout = Workout()


    def parse_name(self):
        """ Parse a Name consisting of one or multiple words """

        name = Name()

        while self.peek().tag == "WORD":
            name.string += self.expect("WORD")
            name.string += " "


        
