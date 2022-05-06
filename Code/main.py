from Code.Compiler import Compiler


file_name = "./Resources/Example.txt"
output_name = "WorkoutProgram"  #name of the output pdf

compiler = Compiler()
compiler.compile(file_name, output_name)
