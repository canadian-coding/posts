""" This is the module/file docstring, this is where you put\
    information about the module/file purpose, as well as information\
    about any global variables.

    NOTE: There are many different 'styles' of docstrings, there are 
    examples of the same class & function(s) in some of the different\
    styles found in the other files in this directory.
"""
# NOTE: it's also worth noting that some people include metadata at the top of their files like author, maintainers etc.
# SEE: http://epydoc.sourceforge.net/manual-fields.html#module-metadata-variables

# For example:
__author__ = "Canadian Coding"
__license__ = "MIT"
__date__ = "2019-07-19"
__version__ = "0.0.1"


class math_operations:
    """
    This is the class docstring, here you can put info about class\
    variables, relevant documentation reference(s), and basic 'quick start'\
    info. You can also mention the purpose of the class here, For example:

    This class takes 2 arguments on instantiation to be used with the\
    remaining class functions to complete simple math operations.
    """
    def __init__(self, x, y):
        """
        Class constructor, takes 2 arguments of arbitrary ints to be\
        used with the other class methods after instantiation.
        """
        # Assign arguments to instance variables
        self.x = x
        self.y = y
    
    def add_x_y(self):
        """
        Takes the provided instance variables, adds them and prints\
        and returns the result.
        """
        print(f"The result of {self.x} + {self.y} is {self.x+self.y}")
        return self.x+self.y

def main(x,y):
    """
    This is a function docstring, it can be used to provide information\
    about function usage, arguments, and function purpose. For example:\
    
    Takes two arguments, both are ints that will be used to instantiate\
    a math_operations instance and run it's add_x_y method.
    """
    example = math_operations(x,y) # Instantiate using provided x, y values
    example.add_x_y() # Run the math_operations instance add_x_y method

if __name__ == "__main__":
    main(4,4)