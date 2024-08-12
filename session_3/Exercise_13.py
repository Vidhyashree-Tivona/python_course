"""Create a module named average with the following functionality:
a) A function that computes the average of numerical values in the list
b) Code to seek user input of 4 values and call the above function and print
the average computed. Use for loop and append method of list class. ( use
range() function to iterate a fixed number of times )
"""


def average(avg_list):
    """Compute average based on the range
    Parameter:
    avg_list - list of values for which average should be calculated
    Result:
    the value of average for the given average list"""
    avg = sum(avg_list) / len(avg_list)
    return avg


def main():
    """Collect user input and use the function above to calculate average
    """
    user_values = []
    for i in range(4):
        values = int(input("Enter the value: "))
        user_values.append(values)
    print("The average is : ", average(user_values))


main()
