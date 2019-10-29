# Generator Expressions & List Comprehensions 

## Description

Generator Expressions & List Comprehensions are syntactically simple ways to create iterables of modified data. They don't **add** any new functionality, they just help to simplify common design patterns and cut down on the amount of code used to implement them.



## Definitions



### Generators

An iterable pseudo-data structure that can act similarly to a list. The main advantage of generators over standard data structures like lists is that they [VASTLY reduce memory usage]( https://code-maven.com/list-comprehension-vs-generator-expression ) (9032 Bytes for the list and 80 bytes for the generator) and computation time because they are not stored in memory. They are calculated on the fly and act similar to a python language-level implementation of [UNIX pipes]( https://en.wikipedia.org/wiki/Pipeline_(Unix) ).



The main disadvantage is that generators **DO NOT** store values, they can be used in place of a list if they only need to be accessed **1** time since the values are generated on the fly (unless the function yielding the generator can be called multiple times).



### List Comprehensions

A syntactically shorter way to produce a list of values with a simple calculation. It is intended to replace the design pattern of:

1. instantiating an empty list
2. Iterate and store values in the list
3. return or use list values.

For example: 

```python
result = [] # 1. Initialize empty list

# 2. Iterate and store values in the list
for number in range(10): # Square numbers from 0-9 and add them to the result list
	result.append(number**2)
	
print(result) # 3. Return or use list values
```



Can be shortened to:



```python
result = [number ** 2 for number in range(10)] # Steps 1-2

print(result) # 3. Return or use list values
```



It does exactly the same as the above example, it is just shorter. The basic syntax is ```[operation for variable in iterable]``` Were operation is the calculation (or function) being run, variable is the name for the temporary iteration variable made, and iterable is some form of iterable (list, generator, set etc.).



### Generator Expressions

Generator expressions follow the same principles as list comprehensions, the primary difference being that the iteration yields a generator object as opposed to a list object. They tend to be more helpful than list comprehensions since they remove the boilerplate code for yielding values. 



Here is an example function that uses the standard yield keyword in conjunction with a function:



```python
def generate_squares():
    """Iterates through 0-9, squares the value and yields it to the generator

    Yields
    ------
    int:
        Square of the current number in the iteration

    """
    for number in range(10):          # loop over 0-9
        yield (number**2)             # Square the number and yield it to the generator

# Uses generator object within function to print squares of 0-9
print("Generator function results:")
for number in generate_squares():
    print(number)
```



The generator expression equivalent is much shorter:

```python
# Uses generator expressions to yield the squares from 0-9
expression_result = (number**2 for number in range(10))

print("\nGenerator expression results:")
for number in expression_result:
    print(number)
```



## Usage



### Running



All of the code in the two demos require no external dependencies, they can be run by using ```python <filename>.py``` or ```python3 <filename>.py```. 



## Real World Applications



The primary purpose of these features in python is to shorten and standardize common design patterns. One problem they both present however is that although convenient to developers who are used to them, they are not intuitive to beginners and so depending on your codebase they may do more harm than good.



Another issue they can present is that the conditions can stack to more than one iterative loop, meaning you can iterate multi-dimensional arrays with this method. If you are at the point of doing this for something more than a 2 dimensional array then, **for the sake of your fellow developers** just do the long way as if I have to read a list comprehension like the one below you will be off my team:

```python
# Generates a 3d array that's 3 sublists of 3 elements 10 times
please_no = [[[element for element in range(3)] for num in range(3)] for sublist in range(10)]
print(please_no)"""prints:
[[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]],[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2],[0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]"""
```

