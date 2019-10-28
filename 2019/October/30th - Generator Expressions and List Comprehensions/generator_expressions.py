"""A demonstration of list comprehensions vs standard iteration.

In this demo the numbers 0-9 are squared and put into a list using
both methods.
"""

def generate_squares():
    """Iterates through 0-9, squares the value and yields it to the generator

    Yields
    ------
    int:
        Square of the current number in the iteration

    """
    for number in range(10):          # loop over 0-9
        yield (number**2)             # Square the number and yield it to the generator

# Uses list comprehensions to generate a list of the squares from 0-9
comprehension_result = (number**2 for number in range(10))

print("Generator function results:")
for number in generate_squares():
    print(number)

print("\nGenerator expression results:")
for number in comprehension_result:
    print(number)
