"""This file is the exact same class defined in dataclass_demo.py
As you can see this class is much longer since you have to implement
both the __init__ and __repr__ methods yourself.
"""

class user:
    def __init__(self, name, age):
        """This class is equivalent to the user dataclass
        defined in dataclass_demo.py
        
        Attributes
        ----------
        name: str
            The users' name

        age: int
            The users' age
            
        Methods
        -------
        __repr__(self)
            prints the instance attributes and type; done by default in a dataclass.
        """
        self.name = name
        self.age = age

    def __repr__(self):
        # Notice the type (user) is hardcoded and would need to be changed in all subclasses
        return f"user(name='{self.name}', age={self.age})" 

if __name__ == "__main__":
    john_doe = user("John Doe", 21)
    print(john_doe)
