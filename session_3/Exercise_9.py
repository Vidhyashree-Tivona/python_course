"""Write a function to do the following:
a) Take a list containing temperatures in fahrenheit
b) The function should return a list containing the temperature in Celsius.
"""


def fahrenheit_to_celsius(fahrenheit_list):
    """Convert fahrenheit to celsius
    Parameter:
    fahrenheit_list - the list of fahrenheit values to be converted to celsius
    Result:
    A list of fahrenheit converted celsius values """
    celsius_list = [(fahrenheit-32) * 5/9 for fahrenheit in fahrenheit_list]
    return celsius_list


values = input("Enter the fahrenheit list of values seperated by spaces: ")
fahrenheit_list = [float(x) for x in values.split()]
print("Temperature in celsius: ", fahrenheit_to_celsius(fahrenheit_list))
