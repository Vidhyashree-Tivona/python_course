"""Write a function to compute and return the median for the values contained
in the given list.
"""


def find_median(values):
    """Compute median for the given list
    Parameter:
    Values - the list of values
    Returns:
    The median value of the given list."""
    n = len(values)
    mid = n // 2
    if n % 2 == 0:
        median = (mid + (mid + 1)) / 2
        return median
    else:
        median = (mid + 0.5) / 2
        return median


list = input("Enter the list of values seperated by spaces: ")
values = [float(x) for x in list.split()]
print(f"The median of the list {values} is {find_median(values)}")
