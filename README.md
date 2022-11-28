# Pipeline Programming Style

## Due Date: Friday December 2nd, 2022 by midnight

## Introduction

In this practical assignment, you will practice writing programs in the Pipeline programming style by converting a program written in the Cookbook programming style to a program that uses the Pipeline programming style. Through this exercise, you will put into practice the following learning objective(s):

- The constraints associated with the Pipeline programming style and how to implement it in Python
- The complexity associated with the Pipeline programming style
- Whether the Pipeline programming style support unit testing

## Instructions

Please perform each of the following steps in order.

### Install Dependencies

Install the dependencies listed in `pyproject.toml` by running `poetry install`.

### Run and Analyze the Cookbook Term Context Program

Run the Cookbook term context program by running `poetry run python term_context_cookbook.py pride_and_prejudice.txt good`. Notice that the high-level behavior of the Cookbook program is identical to the Cookbook program you wrote for the last practical assignment.

Read through the Cookbook program, line-by-line, making sure that you understand how the program produces its output. Then, in `writing/reflection.md`, for each procedure in the Cookbook program, list each global variable that it uses, a description of the global variable's initial value at the beginning of the procedure, a description of the global variable's final value at the end of the procedure, and whether the value of the global variable was changed by the procedure (i.e. the initial value does not equal the final value).

### Convert the Cookbook Program to a Pipeline Program

Take the following steps to convert the Cookbook term context program to a Pipeline term context program.

First, for each function defined in the Pipeline program, copy over its implementation in the Cookbook program.

Then, _for each function_, use the following strategy to determine its input(s) (i.e. parameter(s)) and output.

To determine the input(s) for a function, look at the information about the global variables in the function that you listed in `reflection.md`. If the initial value of a global variable depends on the execution of another function, then add the global variable's name as a parameter to the function. For example, in the `group_char_data_into_words` function, the initial value of `char_data` depends on the execution of the `read_file` function, which populates `char_data`. So, `char_data` should be added as a parameter to the `group_char_data_into_words` function. Additionally, to facilitate unit testing, also add to the parameters any global variables whose initial value is a command-line argument.

Then, for each global variable that has been added as a parameter, remove its `global` statement in the implementation of the function. Finally, complete the `Args` portion of the docstring so that it includes the name and description of each parameter that you added. Use the number of `TODO`s to check that you have added the correct number of parameters.

To determine the output of a function, look again at the information about the global variables in the function that you listed in `reflection.md`. If a global variable's value was changed by the function (i.e. if you wrote "yes" or "true" next to "Value changed?"), then the global variable should be returned by the function. At the end of the function, write a `return` statement that returns this global variable. _Note that the `print_contexts` function will not have a return value._

Referring to `reflection.md`, if the initial value of this global variable at the beginning of the function is a literal (e.g. an empty list), then declare this variable as a local variable with this initial value at the top of the implementation of the function. For example, in the `read_file` function, the initial value of `char_data` is an empty list, `[]`. So, the statement `char_data = []` should be added to the top of the implementation of `read_file`.

Then, remove the `global` statement for this variable. Finally, update the `Returns` portion of the function's docstring with a description of the return value.

After you have set the input(s) and output for each function, call the functions inside the `if __name__ == "__main__":` construct at the bottom of the Pipeline program. The functions should be called in the same order as in the Cookbook program, but they should be called in a "composed" way (i.e. `f(g(x))`), where the input for one function is the output for another. Remember that composed functions are executed starting with the "deepest" composed function; for instance, in `last_function(command_line_argument, first_function(input))`, the `first_function` function is executed first, and then its output is passed to the `last_function` function, which executes next. Any arguments that should be command-line arguments (i.e. from `sys.argv`) should be passed to the functions in this composition. Note that command-line arguments may need to be passed to multiple functions. In the end, your code should look similar to the code from the Pipeline program that is shown in the **Exercises in Programming Style** book:

```python
print_all(sort(frequencies(remove_stop_words(scan(
    filter_chars_and_normalize(read_file(sys.argv[1]))))))[0:25])
```

After you have finished the conversion, make sure the Pipeline program has the same high-level behavior as the Cookbook program by running `poetry run python term_context_cookbook.py pride_and_prejudice.txt good` and `poetry run python term_context_pipeline.py pride_and_prejudice.txt good` in succession and verifying that their outputs are identical.

To further verify the correct behavior of the Pipeline program, execute the test suite by running `poetry run pytest`. Make sure to revise your Pipeline program until all tests pass.

### Reflect on Your Work

Answer all questions in `writing/reflection.md`. As you do, commit your changes using best commit practices. Instead of creating a commit at the end with the message, "Answer reflection questions", you should commit after answering each question and describe your changes in the commit messages.

### Run GatorGrader

You can gain an approximation of your progress on this assignment by running [GatorGrader](https://github.com/GatorEducator/gatorgrader) locally. You do need to have `gatorgrade` and Python installed to be able to run this command.

```bash gatorgrade --config config/gatorgrade.yml

## Receiving Assistance

If you are having trouble completing any part of this project, then please talk with either the course instructor or a student technical leader during the class session. Alternatively, you may ask questions in the Discord channel for this course. Finally, you can schedule a meeting during the course instructor's office hours.

## Practical Assessment

The grade that a student receives on this practical assignment is a checkmark grade (0 or 1) and is based on:

- **GitHub Actions CI Build Status**: Students are encouraged to repeatedly try to complete the assignment until it passes all GitHub Actions jobs. Students will receive a checkmark grade if their last before-the-deadline build passes and a green ✔ appears in their GitHub commit log instead of a red ✗.

Students will receive 1 if their solution passes all GatorGrader checks and receives a green ✔ in their last commit.

All grades for this project will be reported through a student's GitHub gradebook repository.
