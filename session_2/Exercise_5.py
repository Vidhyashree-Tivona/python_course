"""Module to check the divisibilty when two numbers are given.

This module has a function to check the divisibility among two numbers a and b.
"""


def isdivisible(a, b):
    """Check the divisibilty of the given numbers
    Parameters:
    a,b - user input values to check divisibility
    Result:
    Yes if divisible else it prints no
    """
    if (a % b == 0):
        print("Yes, It is divisible"),
    else:
        print("NO, it is not divisible")


a = eval(input("Enter the value of a: "))
b = eval(input("Enter the value of b: "))
isdivisible(a, b)
