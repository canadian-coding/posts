from collections import namedtuple

# Create namedtuple 'Template' 
user = namedtuple("User" ,"name, age, birthday, join_date, premium")

# Allows you to specify IMMUTABLE instances in a class-like syntax
john_doe = user("John Doe", 20, "September 26th 1998", "September 9th 2019", True)

# namedtuple's have a built in __repr__ that is not bad
print(f"There is a user: {john_doe}")

# namedtuple's are also iterable
for attribute in john_doe:
    print(attribute)
