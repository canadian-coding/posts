"""
Description:
    A demo of the ord() and chr() functions in python\
        for ASCII table reference, please visit http://www.asciitable.com/
"""
__author__ = "Canadian Coding"

# chr() takes an int and returns the corresponding ASCII character
print(chr(65)) # prints 'A'
print(chr(97)) # prints 'a'

# ord() takes a one letter string and returns the corresponding ASCII number as an int
print(ord("A")) # Prints 65
print(ord("a")) # Prints 97

def alphabet_by_ord():
    """Goes through and prints the uppercase alphabet using ord() and chr()
    """
    current_letter = ord('A') # Initialize to A
    for letter in range(1,27): #Iterates over all 27 letters of the alphabet
        print(chr(current_letter))
        current_letter += 1 # Move to next letters ordinance

def capitalize_by_ord(letter = "a"):
    """Converts lowercase characters to uppercase using ord() and chr()
    Returns:
        (str): A message with the upper and original case version of the letter
    """
    uppercase_letter = ord(letter) - 32 # Decreasing letters ordinance by offset
    return "Letter {} converted to {}".format(letter, chr(uppercase_letter))

alphabet_by_ord()
print(capitalize_by_ord())