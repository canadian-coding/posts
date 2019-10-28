"""A demonstration of list comprehensions vs standard iteration.

In this demo the numbers 0-9 are squared and put into a list using
both methods.
"""

iterate_result = []                  # Used to store the result of the iterative version
for number in range(10):              # loop over 0-9
    iterate_result.append(number**2) # Square the number and add it to the list

# Uses list comprehensions to generate a list of the squares from 0-9
comprehension_result = [number**2 for number in range(10)]

print(f"Iteration list: {iterate_result}")
print(f"Comprehension list: {comprehension_result}")
