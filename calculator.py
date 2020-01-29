"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
numbers = input(">")


def calc(numbers):
    """Calculator starts here"""
    if ' ' not in numbers:
        return input("Not enough inputs. \n>")

    new_list = numbers.split(" ")
    symbol = ["+", "-", "*", "/", "square", "cube", "pow", "mod"]

    if new_list[0] == "+":
        return add(float(new_list[1]), float(new_list[2]))
    elif new_list[0] == "-":
        return subtract(float(new_list[1]), float(new_list[2]))
    elif new_list[0] == "*":
        return multiply(float(new_list[1]), float(new_list[2]))
    elif new_list[0] == "/":
        return divide(float(new_list[1]), float(new_list[2]))
    elif new_list[0] == "square":
        return square(float(new_list[1]), float(new_list[2]))
    elif new_list[0] == "cube":
        return cube(float(new_list[1]), float(new_list[2]))
    elif new_list[0] == "pow":
        return power(float(new_list[1]), float(new_list[2]))
    elif new_list[0] == "mod":
        return mod(float(new_list[1]), float(new_list[2]))
    else:
        return "Please enter an operator followed by two integers."


print(calc(numbers))