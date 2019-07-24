# Docstrings in python
## Description
Docstrings are an incredibly useful tool in anyone who writes python codes' toolbelt. They are great for letting people know how to use your code. 

You should be using docstrings in **EVERY** class and function definition. Remember that even a poorly styled docstring is better than no context whatsoever so if you are in a hurry at least get the crucial usage details down.

## Definitions

### Docstrings
Docstrings are used to document modules/files, classes, and functions. They help others to understand your code and use it. They are often integrated into IDE's to allow people (and yourself) to quickly see information about using your code including arguments for functions and class instantiation, as well as purpose.

They are also particularly useful for helping **YOU** to remember how your code works after not working on a code base for a while.

Although there are different styles they all follow the same layout outlined in [PEP-257](https://www.python.org/dev/peps/pep-0257/). The format for each type of docstring is as follows:

### Modules/files:
The layout for modules/files is to put the docstring at the top of the file encased in triple quotes. See ```docstrings.py``` for more details.

### Functions
The layout for functions is to put the docstring right after the funcion declaration, the docstring can (should) include information about purpose, usage, arguments, and returm/yield values. For example:
```python
def main(x,y):
    """
    Takes two arguments, both are ints that will be used to instantiate\
    a math_operations instance and run it's add_x_y method.
    """
    example = math_operations(x,y) # Instantiate using provided x, y values
    example.add_x_y() # Run the math_operations instance add_x_y method
```

### Classes:
 There are two optional layouts (note that both are often implemented in IDE's and autodocumentation generators). 

1. The first layout is class definition followed on the next line by triple quotes and the information. For example:
```python
class math_operations:
    """
    This class takes 2 arguments on instantiation to be used with the remaining class functions to complete simple math operations.
    """
```

2. The second layout is to use the class constructors' docstring to contain the class information.
```python
class math_operations:
    def __init__(self, x, y):
        """
        This class takes 2 arguments on instantiation to be used with the remaining class functions to complete simple math operations.
        """
        # Assign arguments to instance variables
        self.x = x
        self.y = y
```

### Style Guides
Style guides are conventions for formatting code. They are prevelant in all languages, there are a few different ones in python, I have outlined a couple of the more popular ones for python later in this file.

## Usage
The demos in this repo are to show off a simple example of module/file, class and function docstrings in multiple styles.

### Running
Although running the demos are not the point, you can run each file using ```python <filename>.py```.

## Real World Applications
Docstrings (and documentation in general) are an essential part of large projects, without them code becomes completely unmanageable, especially for external contributors.

## Additional information
### PEP-8
[PEP-8](https://www.python.org/dev/peps/pep-0008/) is a popular python style guide, it is very useful for styling python code. Particularly for this demo https://www.python.org/dev/peps/pep-0008/#documentation-strings may be helpful.

### Docstring styles
There are multiple different 'styles' of docstrings, although (as far as I know) there is no official 'style' I have provided information on the three most popular styles below.

#### reStructuredtext Style
This style is often the 'preffered' style in the python community as it is the most
prominent style used for sphinx (http://www.sphinx-doc.org/en/master/index.html) autodocumentation.

For more details about reStructuredtext.
SEE: http://docutils.sourceforge.net/rst.html

Example function:

```python
def main(x,y):
    """
    Instantiates a math_operations instance using the provided values and runs the instance add_x_y method.

    :param x: an arbitrary number to be used in instantiating a math_operations instance
    :type x: int or float

    :param y: an arbitrary number to be used in instantiating a math_operations instance
    :type y: int or float
    """
```

#### Google Style
This style is my preffered style for it's easy readability and flexibility.

For more details about the full google style guide.
http://google.github.io/styleguide/pyguide.html

For details about google style docstrings 
http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings

Example function:

```python
def main(x,y):
    """
    Instantiates a math_operations instance using the provided values and runs the instance add_x_y method.

    Args:
        x(int or float): an arbitrary number to be used in instantiating a math_operations instance
        y(int or float): an arbitrary number to be used in instantiating a math_operations instance
    """
```

#### numpy Style
This style is used heavily in scientific and complex caculation libraries.

For details about numpy style docstrings https://numpydoc.readthedocs.io/en/latest/format.html

Example function:

```python
def main(x,y):
    """
    Instantiates a math_operations instance using the provide values and runs the instance add_x_y method.

    Parameters
    ----------
        x : int or float
            an arbitrary number to be used in other instance methods
        y : int or float
            an arbitrary number to be used in other instance methods
    """
```