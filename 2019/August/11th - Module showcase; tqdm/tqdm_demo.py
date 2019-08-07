from tqdm import tqdm # The module relies on a class called tqdm inside the module
import time # Used to delay iteration to make the progress bar more easily visible

# Un-fortmatted tqdm progress bar
print("Here is your standard tqdm bar:")
for iteration in tqdm(range(10)):
    time.sleep(.3)

# Example of a formatted tqdm bar
print("Here is a custom formatted tqdm bar:")
iterable = tqdm(range(100)) # Setting iterable wrapped in tqdm as a variable
for amount_complete in iterable: # This demo is based on https://github.com/tqdm/tqdm#iterable-based
    time.sleep(0.25)
    iterable.set_description(f"Currently at %{amount_complete}") # Allows you to overwrite the default printing style provided by tqdm
