from collections import Counter

# Instantiate a counter instance with a list
fruit_counter = Counter(['apple','orange','banana','apple'])

# You can also create/update counters with keyword arguments
fruit_counter.update(banana=75, apple=3)

# You can also use a dictionary
fruit_counter.update({"orange":45, "banana":113, "apple":90})

# Default __repr__ prints all items and their counts
print(f"Fruit counter: {fruit_counter}")

# instance.most_common() prints elements in descending order
print(f"Most common: {fruit_counter.most_common()}")

