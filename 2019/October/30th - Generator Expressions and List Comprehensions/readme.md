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

...



## Usage



### Running



All of the code in the two demos require no external dependencies, they can be run by using ```python <filename>.py``` or ```python3 <filename>.py```. 



## Real World Applications



...