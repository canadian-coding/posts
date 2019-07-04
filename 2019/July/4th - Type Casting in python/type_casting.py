"""
Description:
    A demo of type casting in python 3.

    The preferred method of type casting is to use the type hint\
        as a function around the variable you want to cast
"""
__author__ = "Canadian Coding"

my_string = "1"
print(type(my_string) == str) # returns True

# Convert my_string to an int
my_string = int(my_string)
print(type(my_string) == int) # returns True

# When something cannot be type casted it will raise an exception
my_string = list(my_string) # raises TypeError

# An example where the error is caught
my_string = "hello"
try:
    my_string = int(my_string) # raises value error
except ValueError:
    print("HEY, {} can't be made into an int".format(my_string))
