"""Write a function to compute and return the mode for the values contained in
the given list."""


import statistics


def find_mode(values):
    """Funtion to find mode for the given list
    Parameter:
    values - the list of values
    Result:
    The mode of the given list values"""
    try:
        mode_value = statistics.mode(values)
        return mode_value
    except statistics.StatisticsError as e:
        return str(e)


def main():
    """Function to take user input"""
    user_input = input("Enter the list of values separated by spaces: ")
    try:
        values = [float(x) for x in user_input.split()]
        if not values:
            print("The list is empty. Please enter some values.")
            return
        print(f"The mode of the list {values} is {find_mode(values)}")
    except ValueError:
        print("Please enter numeric values only.")


main()
