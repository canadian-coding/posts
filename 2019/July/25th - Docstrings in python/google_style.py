""" This file is here to demonstrate the Google style of docstrings.

This style is my preffered style for it's easy readability and flexibility.

For more details about the full google style guide.
SEE: http://google.github.io/styleguide/pyguide.html

For details about google style docstrings 
SEE: http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
"""

class math_operations:
    """
    There are two options for documenting the overall class. You can include
    all the information about the class purpose, instance/class paramaters, and
    contructor details, before the __init__ mehod or as the __init__ methods' docstring.
    In this example file I have done both. Also notice that when using the docstring outside
    the __init__ method the heading changes from Args to attributes.

    Attributes:
        x(int or float): an arbitrary number to be used in other instance methods
        y(int or float): an arbitrary number to be used in other instance methods
    """
    def __init__(self, x, y):
        """
        There are two options for documenting the overall class. You can include
        all the information about the class purpose, instance/class paramaters, and
        contructor details, before the __init__ mehod or as the __init__ methods' docstring.
        In this example file I have done both.

        Args:
            x(int or float): an arbitrary number to be used in other instance methods
            y(int or float): an arbitrary number to be used in other instance methods
        """
        # Assign arguments to instance variables
        self.x = x
        self.y = y
    
    def add_x_y(self):
        """
        Takes the provided instance variables, adds them and prints
        and returns the result.

        Returns:
            int: The result of adding the instances x and y variables
        """
        print(f"The result of {self.x} + {self.y} is {self.x+self.y}")
        return self.x+self.y

def main(x,y):
    """
    Instantiates a math_operations instance using the provided values
    and runs the instance add_x_y method.

    Args:
        x(int or float): an arbitrary number to be used in instantiating a math_operations instance
        y(int or float): an arbitrary number to be used in instantiating a math_operations instance
    """
    example = math_operations(x,y) # Instantiate using provided x, y values
    example.add_x_y() # Run the math_operations instance add_x_y method

if __name__ == "__main__":
    main(4,4)