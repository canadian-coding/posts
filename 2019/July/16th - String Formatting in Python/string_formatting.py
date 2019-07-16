"""
Description:
    A demo of the 4 primary methods of string formatting.
"""
name = "John Smith" # A dummy name
email_count = 3 # A representation of users # of new emails
current_temperature = 20.3567 # A representation of the current temperature in celsius 

##### ===== New/Current Style ===== #####
""" fstrings/string interpoloation; This is the most current way of doing things,
    it allows you to use embedded variable calls using {variable_name}
 SEE: https://docs.python.org/3/whatsnew/3.6.html#pep-498-formatted-string-literals """
greeting = f"Hello, {name} The weather today is {current_temperature} degrees. You have {email_count} new emails."
print(greeting)

"""
format function; Allows you to put placeholders {} to be filled as arguments during the function call
SEE: https://docs.python.org/3.4/library/string.html#format-examples for more examples
"""
greeting = "Hello, {} The weather today is {:03.2f} degrees. You have {} new emails.".format(name, current_temperature, email_count)
print(greeting)

##### ===== Old Style ===== #####
# % formatting;
greeting = "Hello, %s The weather today is %03.2f degrees. You have %d new emails." % (name, current_temperature, email_count)
print(greeting)

# +; you can concatenate strings together using the + operator. NOTE: This uses the string classes' __add__ method.
greeting = "Hello, " + name + " The weather today is " + str(current_temperature) + " degrees. You have " + str(email_count) + " new emails."
print(greeting)