""" This file is here to demonstrate the reStructured Text style of docstrings.

This style is often the 'preffered' style in the python community as it is the most
prominent style used for sphinx (http://www.sphinx-doc.org/en/master/index.html) autodocumentation.

For more details about reStructuredtext.
SEE: http://docutils.sourceforge.net/rst.html

For details about docstrings in general SEE: docstrings.py and readme.md
"""

class math_operations:
    """
    There are two options for documenting the overall class. You can include
    all the information about the class purpose, instance/class paramaters, and
    contructor details, before the __init__ mehod or as the __init__ methods' docstring.
    In this example file I have done both.

    :param x: an arbitrary number to be used in other instance methods
    :type x: int or float

    :param y: an arbitrary number to be used in other instance methods
    :type y: int or float
    """
    def __init__(self, x, y):
    """
    There are two options for documenting the overall class. You can include
    all the information about the class purpose, instance/class paramaters, and
    contructor details, before the __init__ mehod or as the __init__ methods' docstring.
    In this example file I have done both.

    :param x: an arbitrary number to be used in other instance methods
    :type x: int or float

    :param y: an arbitrary number to be used in other instance methods
    :type y: int or float"""
        # Assign arguments to instance variables
        self.x = x
        self.y = y
    
    def add_x_y(self):
        """
        Takes the provided instance variables, adds them and prints
        and returns the result.

        :returns: The result of adding the instances x and y variables
        :rtype: int
        """
        print(f"The result of {self.x} + {self.y} is {self.x+self.y}")
        return self.x+self.y

def main(x,y):
    """
    Instantiates a math_operations instance using the provided values
    and runs the instance add_x_y method.

    :param x: an arbitrary number to be used in instantiating a math_operations instance
    :type x: int or float

    :param y: an arbitrary number to be used in instantiating a math_operations instance
    :type y: int or float
    """
    example = math_operations(x,y) # Instantiate using provided x, y values
    example.add_x_y() # Run the math_operations instance add_x_y method

if __name__ == "__main__":
    main(4,4)