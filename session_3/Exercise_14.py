"""Modifying the exercise_13 module to keep the size of the list of values
flexible. Use a while loop to allow the user to enter any number of values
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
    print("Enter the values \nType 'done' when you are finished")
    while True:
        values = input("Enter the value: ")
        if values.lower() == 'done':
            break
        user_input = float(values)
        user_values.append(user_input)
    if user_values:
        print("The average is", average(user_values))
    else:
        print("No values entered")


main()
