"""Module to calculate the selling price with certain parameters.


This module has a function to calculate the selling price based on the binding
type.
"""


def selling_Price(list_price, binding_type, discount_percentage):
    """Calculating the selling price
    Paramters:
    List price - The original list price of the item.
    discount_percentage - The discount value to be applied
    binding_type - The type of binidng either HB or PB
    Result:
    The selling price after the discount if applicable.
    """
    if binding_type.upper() == "HB":
        selling_Price = list_price
    elif binding_type.upper() == "PB":
        discount = discount_percentage/100
        selling_Price = list_price * (1-discount)
    else:
        print("Select the correct binding type eg. HB or PB")
        return None
    return selling_Price


list_price = eval(input("Enter the list price value: "))
binding_type = input("Enter the binding_type: ").strip()
discount_percentage = 0

if binding_type.upper() == "PB":
    discount_percentage = eval(input("Enter the discount percentage: "))


print("The selling price = ", selling_Price(list_price, binding_type,
                                            discount_percentage))
