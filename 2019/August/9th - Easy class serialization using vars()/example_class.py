"""
This file is here to create a sample class to show off the vars() method
"""

class user:
    def __init__(self, name, age, birthday, country, address):
        """
        A generic user class to store information about people.

        Parameters
        ----------
            name : string
                User instances' name
            age : int
                User instances' age
            birthday : string
                User instances' birthday
            Country : string
                User instances' current country location
            address : string
                User instances' address
        """
        self.name = name
        self.age = age
        self.birthday = birthday
        self.country = country
        self.address = address
