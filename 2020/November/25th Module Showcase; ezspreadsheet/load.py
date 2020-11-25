from dataclasses import dataclass
from ezspreadsheet import Spreadsheet

@dataclass
class User():
    Name:str
    Age:int
    Weight:int
    Family: list

file_path = "users.xlsx" # also works with .csv

# Retrieve namedtuple classes when class constructor is available
with Spreadsheet(file_path, User) as input_sheet:
    users, instances = input_sheet.load("users")
print(instances) # [User(Name='Kieran', Age=21, Weight=202, Family=['sister', 'mother', 'father']), User(Name='Jim', Age=12, Weight=170, Family=['brother', 'mother', 'father'])]
print(users == User) # True

# Retrieve namedtuple classes when no class constructor is available
with Spreadsheet(file_path) as input_sheet:
    users, instances = input_sheet.load("users")
print(instances) # [users(Name='Kieran', Age=21, Weight=202, Family=['sister', 'mother', 'father']), users(Name='Jim', Age=12, Weight=170, Family=['brother', 'mother', 'father'])]
print(users == User) # False