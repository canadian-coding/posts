# Type Hinting and Type Checking in python

## Description

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
In this repo you can see the demo code and actually run it by running ```python type_cheking.py``` or ```python3 type_cheking.py```.

## Real World Applications
If you are writing API's that are meant to work with with various data types then type checking is a good way to validate input. **KEEP IN MIND** type checking is expensive in terms of computation so avoid using it as much as possible. A common pattern to avoid is checking types in a loop.

For example:
```python
data = {"URL": ["google.ca", "youtube.com", "facebook.com"], 
    "Company": ["Google", "Google", "Facebook"]}

for counter in range(len(list(data.keys())[0])): # Iterates over whole list/generator
    for key in data:
        # Check if value of key is a list or generator
        if type(data[key]) is list:
            # Do stuff

        elif isinstance(data[key], types.GeneratorType):
            # Do stuff
```

Because python is checking on every iteration this loop would be **VERY** slow. A better option would be something like this:

```python
data = {"URL": ["google.ca", "youtube.com", "facebook.com"], 
    "Company": ["Google", "Google", "Facebook"]}

# Set up boolean values to keep track of value types
is_list = False
is_generator = False


for key in data: # Do an initial pass to check types
    if type(data[key]) is list:
        is_list = True
    elif isinstance(data[key], types.GeneratorType):
        is_generator = True
    else:
        raise TypeError("An invalid type was provided")
for counter in range(len(list(data.keys())[0])): # Iterates over whole list/generator
for key in data:
        # Check if value of key is a list or generator
        if is_list:
            # Do stuff

        elif is_generator:
            # Do stuff
```

Because you are only doing 1 type check at the beginning this would be much faster.