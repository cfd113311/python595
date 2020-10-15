# 10 pts
# Please implement the following.
# 5 pts for code, 5 pts for style.

import sys

def parse_command_line(rawinput):
    '''
    parse_command_line takes the commandline
    arguments of sys.argv.

    It returns useful errors.

    This command is executed from the commandline.

    For example:
    python celsius.py 86

    Will print:
    "86F is 30C"

    A wrong case is a user typing too
    many inputs.
    python celsius.py 85 38

    This should return an error.

    Can your code handle negative Fahrenheit values?
    The raw input is a string.
    How can we convert a string to a floating point
        number?

    Good luck!
    '''
    if len(rawinput) != 2:
        raise IOError("This program converts one and only one " +
                      "fahrenheit reading to celsius.")

    try:
        degree_fahrenheit = float(rawinput[1])
    except ValueError:
        raise ValueError("The input must be a number. Make sure " +
                         "you didn't include a units designation.")

    return degree_fahrenheit


def calculate_celsius(degree_fahrenheit):
    '''
    Print conversion after parse.
    '''
    degree_celsius = (degree_fahrenheit-32) * 5/9
    print(f"{degree_fahrenheit:g}F is {degree_celsius:g}C")


if __name__ == "__main__":
    command_line_inputs = sys.argv
    user_fahrenheit = parse_command_line(command_line_inputs)
    calculate_celsius(user_fahrenheit)
