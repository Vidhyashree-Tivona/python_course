"""Write a function that returns a list of random integers. The length of list
is to be provided as an argument"""

import random


def generate_random(length):
    """Generate random numbers based on the arguments
    Parameters:
    length - the number of integers need to be in the list
    Result:
    A list of randomly generated numbers."""
    random_list = []
    for i in range(length):
        random_number = random.randint(1, 30)
        random_list.append(random_number)
    return random_list


print("The random numbers generated = ", generate_random(10))
