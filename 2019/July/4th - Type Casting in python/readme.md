# Type Hinting and Type Checking in python

## Description

### Type Casting
When you convert a variable/object to another type. For example:
```python 
my_string = "0" # my_string is a str type
type(my_string) == str # Returns True since my_string is a str
type(my_string) == int # Returns False since my_string is a str

my_string = int(my_string) # type casting my_string to an int
type(my_string) == str # Returns False since my_string is now an int
type(my_string) == int # Returns True since my_string is now an int
```

### Type hinting
Is the mechanism in python that allows you to know what type a variable is. Each created object in python has a type including the builtin types like dict and list. See this cheatsheet as reference for full details [here](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html).  

### Type Checking
Is a method of validating that a variable is of a certain expected type. There are multiple ways of doing this. For Example:
```python
my_list = ["hello"] # Returns <class 'list'>
type(my_list) == list # Returns True
```
Some types require a more exotic form of type checking such as generators, to type check generators for example:
```python
import types
def yield_numbers(amount = 10):
    for i in range(amount):
        yield i

isinstance(yield_numbers(), types.GeneratorType) # Returns True
```
## Usage
In this repo you can see the demo code and actually run it by running ```python type_casting.py``` or ```python3 type_casting.py```.

## Real World Applications
**KEEP IN MIND** type casting is expensive in terms of computation so avoid using it as much as possible. If a process can be done with the type already provided avoid doing the unnecessary type casting.