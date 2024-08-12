"""Write a function to return a list of even numbers. The size of the list is
to be given as an argument to the function"""


def even_numbers(length):
    """Generate a list of even numbers
    Parameter:
    length - the numbers of integers in the list
    Result:
    A list of even integers."""
    even_values = []
    current_no = 0
    while len(even_values) < length:
        even_values.append(current_no)
        current_no += 2
    return even_values


length = int(input("Enter the value for length of list: "))
print("The list of even numbers generated = ", even_numbers(length))
