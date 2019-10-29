"""A demonstration of generator expressions vs function yielding.

In this demo the numbers 0-9 are squared and yielded to a generator using
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

# Uses generator expressions to yield the squares from 0-9
expression_result = (number**2 for number in range(10))

print("Generator function results:")
for number in generate_squares():
    print(number)

print("\nGenerator expression results:")
for number in expression_result:
    print(number)
