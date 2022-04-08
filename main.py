import sys
from Code.Lexer import Lexer
from Code.Parser import Parser
from Code.PrettyPrinter import PrettyPrinter
from Code.Visitor import Visitor

from pprint import pprint


file_name = "Resources/Example.txt"

try:
    with open(file_name, 'r') as file:
        file_data = file.readlines()
except FileNotFoundError:
    print('Error: test file {} does not exist'.format(file_name))
    sys.exit()

lexer = Lexer()
lexed = lexer.lex(file_data)
print("\n")
print(lexed)
print("\nLexer: analysis successful!")

parser = Parser()
ast = parser.parse(lexed)
print(vars(ast))
print("\nParser: analysis successful!")

visitor = Visitor()
visitor.visit(ast)

pp = PrettyPrinter()
pp.prettyPrint(ast)
