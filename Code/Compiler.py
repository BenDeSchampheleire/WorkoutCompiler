import sys

from Code.GeneratorPDF import GeneratorPDF
from Code.Lexer import Lexer
from Code.Parser import Parser
from Code.PrettyPrinter import PrettyPrinter
from Code.Visitor import Visitor


class Compiler:

    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()
        self.visitor = Visitor()
        self.prettyprinter = PrettyPrinter()
        self.generator = GeneratorPDF()

    def compile(self, file_name, output_name):

        try:
            with open(file_name, 'r') as file:
                file_data = file.readlines()
        except FileNotFoundError:
            print('Error: test file {} does not exist'.format(file_name))
            sys.exit()

        lexed = self.lexer.lex(file_data)
        print("\nLexer: analysis successful!")

        ast = self.parser.parse(lexed)
        print("\nParser: analysis successful!\n")

        self.visitor.visit(ast)
        print("\nVisitor: analysis successful!")

        self.prettyprinter.prettyPrint(ast)

        self.generator.generatePDF(ast, output_name)
        print("\nPDFGenerator: analysis successful!")
