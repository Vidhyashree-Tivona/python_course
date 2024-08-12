"""Module to find the largest among the three numbers.

This Module has a function to find the largest number.
"""


def largest_number(a, b, c):
    """Check the largest number among the three user input values.
    Parameters:
    a,b,c - user input values to evaluate the largest number
    returns:
    The largest number among the three user input values.
    """
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


a = eval(input("Enter the value of a: "))
b = eval(input("Enter the value of b: "))
c = eval(input("Enter the value of c: "))
print("The largest number = ", largest_number(a, b, c))
