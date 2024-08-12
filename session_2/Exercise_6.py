"""Module to calculate the selling price when the list price is given.


This module has a function to calculate the selling price assuming the
discount as 10%.
"""


def selling_Price(list_price):
    """Calculating the selling price
    Paramters:
    Discount - 10%
    List price - the value of list price of the item.
    Result:
    The selling price after the discount.
    """
    discount = 0.10  # Assuming the discount is 10%
    SP = list_price * (1 - discount)
    return SP


list_price = eval(input("Enter the list price value: "))
print("The selling price = ", selling_Price(list_price))
