import sys
from Code.Lexer import Lexer

file_name = "Resources/Example.txt"

try:
    with open(file_name, 'r') as file:
        file_data = file.readlines()
except FileNotFoundError:
    print('Error: test file {} does not exist'.format(file_name))
    sys.exit()

lexer = Lexer()
lexed = lexer.lex(file_data)
print(lexed)
