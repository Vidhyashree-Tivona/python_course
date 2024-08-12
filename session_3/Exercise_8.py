"""Write a function to do the following:
 a) A list of distances in miles will be provided as an argument
 b) The function should return a list containing the same values converted to
 Kilometers
"""


def miles_to_km(miles_list):
    """Convert miles to kilometers
    Parameters:
    miles_list - The list of miles value that must be coverted to kilometers
    Return:
    A list of distance converted to kilometers"""
    # Conversion factor
    conversion_factor = 1.60934
    kilometers_list = [miles * conversion_factor for miles in miles_list]
    return kilometers_list


values = input("Enter the miles list of values seperated by spaces: ")
miles_list = [float(x) for x in values.split()]
print("Distance in kilometers: ", miles_to_km(miles_list))
