"""Module to check if the user input is either a vowel or not.


This module has a function which is used to check the vowel.
"""


def find_vowel(x):
    """check if a given paramter is vowel.
    Parameters:
    x: A single character to check
    Returns:
    bool: True if the character is vowel both lowercase and uppercase.
    """

    vowels = "aeiouAEIOU"
    return x in vowels


x = input("Enter a character: ")
print(find_vowel(x))
