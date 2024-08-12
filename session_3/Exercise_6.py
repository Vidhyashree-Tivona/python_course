"""Write a function that returns a list of random integers. The length of list
is to be provided as an argument"""

import random


def generate_random__numbers(length, min_value=0, max_value=100):
    """Generate random numbers based on the arguments
    Parameters:
    length - the number of integers need to be in the list
    min_value - the minimum value of integers
    max_value - the maximum value of integers
    Result:
    A list of randomly generated numbers."""
    if min_value < 0 or max_value > 100:
        return "Error: the minimum value should be >=0 and maximum value <=100"
    if min_value > max_value:
        return "Error: Minimum value should not be greater than maximum value"
    random_list = []
    for i in range(length):
        random_number = random.randint(min_value, max_value)
        random_list.append(random_number)
    return random_list


length = int(input("Enter the value for length of the list: "))
min_value = int(input("Enter minimum value it should not be lesser than 0: "))
max_value = int(input("Enter maximum value it should not exceed value 100: "))
print("The random numbers generated = ", generate_random__numbers
      (length, min_value, max_value))
