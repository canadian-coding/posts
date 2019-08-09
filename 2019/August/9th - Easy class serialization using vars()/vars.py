"""A demo of the vars function, specifically it's usage to expedite JSON serialization
vars() is a function that takes an object instance as an argument and returns a dict
of the instance attributes.

SEE: vars documentation https://docs.python.org/3/library/functions.html#vars
"""
import json # Used to serialize data to a JSON file SEE: https://docs.python.org/3/library/json.html
from example_class import user # Dummy class to instantiate, and serialize

example_user = user("John Doe", 21, "22-10-1995", "Australia", "123 Main Street") # Instantiate an example to use later

print("User class vars output: ")
# outputs: {'name': 'John Doe', 'age': 21, 'birthday': '22-10-1995', 'country': 'Australia', 'address': '123 Main Street'}
print(vars(example_user))

# You can use vars with json.dump to serialize a class instance to a json file
json.dump(vars(example_user), open("user.json", "w")) 
