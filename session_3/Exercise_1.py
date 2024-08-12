"""Write a function to find the selling price of the book when the list price
and discount_percentage are given. Discount percentage should be optional.
When no value is provided, the function will assume that the value is 10%
"""


def selling_price(list_price, discount_percentage=10):
    """Calculating the selling price based on list price and discount p
    ercentage
    Parameters:
    list_price - The original list price of the item
    discount_percentage - The discount value to be applied if not the default
    value becomes 10%
    Results:
    THe selling price after the discount if applicable"""
    SP = list_price * discount_percentage/100
    return SP

# Obtain user input to calculate the selling price


list_price = int(input("Enter the list price value: "))
discount_percentage = int(input("Enter the discount percentage: ") or 10)
print(selling_price(list_price, discount_percentage))
