""" This file is here to demonstrate the Numpy style of docstrings.

This style is used heavily in scientific and complex caculation libraries.

For details about numpy style docstrings 
SEE: https://numpydoc.readthedocs.io/en/latest/format.html
"""

class math_operations:
    """
    There are two options for documenting the overall class. You can include
    all the information about the class purpose, instance/class paramaters, and
    contructor details, before the __init__ mehod or as the __init__ methods' docstring.
    In this example file I have done both. Also notice that when using the docstring outside
    the __init__ method the heading changes from Parameters to Attributes.

    Attributes
    ----------
        x : int or float
            an arbitrary number to be used in other instance methods
        y : int or float
            an arbitrary number to be used in other instance methods
    """
    def __init__(self, x, y):
        """
        There are two options for documenting the overall class. You can include
        all the information about the class purpose, instance/class paramaters, and
        contructor details, before the __init__ mehod or as the __init__ methods' docstring.
        In this example file I have done both.

        Parameters
        ----------
            x : int or float
                an arbitrary number to be used in other instance methods
            y : int or float
                an arbitrary number to be used in other instance methods
        """
        # Assign arguments to instance variables
        self.x = x
        self.y = y
    
    def add_x_y(self):
        """
        Takes the provided instance variables, adds them and prints
        and returns the result.

        Returns
        -------
            int or float
                The result of adding the instances x and y variables
        """
        print(f"The result of {self.x} + {self.y} is {self.x+self.y}")
        return self.x+self.y

def main(x,y):
    """
    Instantiates a math_operations instance using the provided values
    and runs the instance add_x_y method.

    Parameters
    ----------
        x : int or float
            an arbitrary number to be used in other instance methods
        y : int or float
            an arbitrary number to be used in other instance methods
    """
    example = math_operations(x,y) # Instantiate using provided x, y values
    example.add_x_y() # Run the math_operations instance add_x_y method

if __name__ == "__main__":
    main(4,4)