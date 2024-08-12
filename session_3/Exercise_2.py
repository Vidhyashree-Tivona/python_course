"""Write a function to compute and return the arithmetic mean for the values
contained in the given list.
"""


def arithmetic_mean(values):
    """Compute arithemtic mean for the given list of values
    Parameter:
    Values - the list of values
    returns:
    The arithmetic mean value for the given list
    """
    arith_mean = sum(values)/len(values)
    return arith_mean


list = input("Enter the list of values seperated by spaces: ")
values = [float(x) for x in list.split()]
print(f"The arithmetic mean of the list {values} is {arithmetic_mean(values)}")
