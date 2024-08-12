"""Module to calculate the simple interest.


This module has a function simple interest for calculating the same.
"""


def simple_interest(p, n, r):
    """Calculate the Simple interest.
    Parameters:
    p - An integer value which is the principal amount
    n - An integer value which is the number of years
    r - An integer value which is the rate of interest."""
    SI = (p * n * r)/100
    return SI


p = eval(input("Enter the principal amount: "))
n = eval(input("Enter the Number of years: "))
r = eval(input("Enter the rate of interest: "))
print("Simple interest = ", simple_interest(p, n, r))
