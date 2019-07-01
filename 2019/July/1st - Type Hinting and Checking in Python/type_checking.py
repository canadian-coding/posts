"""
Description:
    A demonstration of type checking
"""
__author__ = "Canadian Coding"

# Type Hinting/Checking on a list
my_list = ["hello"] # Returns <class 'list'>
type(my_list) == list # Returns True

# Type Checking Generators
import types # Need to explicitly import types to check generators
def yield_numbers(amount = 10):
    """A dummy function that yields a generator of ints as an example
    Yields:
        Incrementing integers up to amount provided
    """
    for i in range(amount):
        yield i

isinstance(yield_numbers(), types.GeneratorType) # Returns True