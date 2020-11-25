from dataclasses import dataclass
from ezspreadsheet import Spreadsheet

@dataclass
class User(): # Setup class to store instances of
    Name:str
    Age:int
    Weight:int
    Family: list

file_path = "users.xlsx" # also works with .csv

user_1 = User("Kieran", 21, 202, ["sister", "mother", "father"])
user_2 = User("Jim", 12, 170, ["brother", "mother", "father"])

with Spreadsheet(file_path, User) as output_file:
    # Can also pass a list or tuple of intances such as [user_1, user_2]
    output_file.store(user_1, user_2)

