"""This file is meant to demonstrate the usefullness of dataclasses.
dataclasses allow you to create short, simple and useful classes. By
default decorating a class as a dataclass will automatically create a
__init__ and __repr__ method based on the class attributes.
"""
from dataclasses import dataclass # import dataclass method from module

@dataclass # Decorate class to let python know this is a dataclass
class user:
    """This is a demo class of a basic user.
        
        Attributes
        ----------
        name: str
            The users' name

        age: int
            The users' age"""
    name: str
    age: int

if __name__ == "__main__":
    john_doe = user("John Doe", 21)
    print(john_doe)
