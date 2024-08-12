import math

"""Module related to Calculating area and circumference of circle using
math library.

This module contains two functions area_circle and circumference_circle for
calculating area and circumference of circle respectively.

"""


def area_circle(radius):
    """ Function used to calculate area of circle which has the parameter
    named radius and the imported math library assigns the value of pi.
    """

    area_of_circle = math.pi * radius ** 2
    return area_of_circle


def circumference_circle(radius):
    """ Calculate area and circumference of circle
    Paramter:
    radius: A single integer value to calculate
    returns:
    The value of area of circle and circumference of circle is calculated.
    """

    circumference_of_circle = 2 * math.pi * radius
    return circumference_of_circle


# obtain user input for radius
radius = eval(input("Enter the value of radius: "))
print("Calculating the area and circumference of circle")
print("____________________________________________________\n")
print("The area of circle = ", area_circle(radius))
print("The circumference of circle = ", circumference_circle(radius))
