""" Description:
        A demo of codetags used in inline comments and docstrings.
"""
import os # Used to demo the PORT CodeTag with os specific implementations

class User:
    def __init__(self,name):
        """
        DOCUMENT: Write docstring

        TODO: Come up with full list of class attributes

        REQ: Store user information such as name, birthday, city etc.

        Arguments:
        name(str): The name of the user. NOTE: Name implies first name, not necessarily full name
        """
        # TODO: Assign name to self.name
        q # BUG: will cause an error until removed

if os.name == "nt": # PORT: only runs if on windows
    print("You are on weindows") # FIXME: Fix spelling of windows
    
else: # PORT: only runs if not on windows
    print("You are on linux/mac")
