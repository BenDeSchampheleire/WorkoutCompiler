# WorkoutCompiler

---
Workout Compiler allows the user to easily create custom workout programs using the proposed syntax.
An example is given in th file `Example.txt`:

```
Program("Muscle Gain") {
    Workout("Shoulder") {
        Exercise("incline barbell bench press", 3, 12, 90);
        Exercise("flat dumbbell bench press", 3, 12, 90);
        Exercise("cable crossover", 3, 12, 90);
        Exercise("seated lateral raise", 3, 12, 90);
        Exercise("single arm cable lateral raise", 3, 12, 90);
    }
    Workout("Chest") {
        Exercise("push-ups", 3, 12, 90);
    }
}
```

To compile this example, run the file `main.py`. The output is stored in `WorkoutProgram.pdf`.

**Note**: the Compiler only allows to compile one program at a time

## Workflow

First, the input text is cut into Tokens by a `Lexer`.
Then, a `Parser` will verify if the imposed syntax is respected and create an Abstract Syntax Tree (AST).
Next, the Syntax Tree will be visited by multiple Visitor: a dummy `Visitor`, a `PrettyPrinter` and a `PDF Generator`.
1. The dummy `Visitor` will print which nodes of the AST have been visited.
2. The `PrettyPrinter` will reshape the AST into well-structured lines of code, resembling a pretty version of the input.
3. The `PDF Generator` will create a pdf file containing the Program with all the Workouts and Exercises.

The `Compiler` class contains all the previous steps.

## PDF Generation

The way in which the pdfs are generated is rather particular.
For every Workout in the Program, a new page is created.
The Exercise of a certain Workout are arranged per four in line.
In order to make the pdf visually more attractive, images are used from the online database of `bodybuilding.com`.
The compiler make a query to the database with the name of the exercise and recovers the first image from the HTML code.
This image is then used in the pdf.
If no search results are found, "No search results" is printed instead of an image.
In order to facilitate the use of the compiler, every image that is used in the pdf is stored in a local database.
This speeds up the compiler and makes it more proficient every time it is used.

## Documentation

For more info on the different classes and methods, open the [documentation](https://htmlpreview.github.io/?https://github.com/BenDeSchampheleire/WorkoutCompiler/blob/main/Docs/build/index.html).