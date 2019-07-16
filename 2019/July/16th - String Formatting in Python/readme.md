# String Formatting and Literals

## Description
String formatting and Literals are incredibly useful tools for building dynamic strings in python programs. They allow you to build strings using variable input, and change the default behaviour of strings respectively.

## Definitions

### String Prefixes/String Literals
In python there are a set of prefixes (string literals) that create completely different effects. For example placing an r or R in front of a string instantiation will cause it to ignore special characters such as \n or \t. 

Example:
```python
my_string = "Hello \n\tWorld" 
print(my_string) """Would print:
Hello 
    World """

my_string = r"Hello \n\tWorld" # Also works with R"Hello \n\tWorld"
print(my_string) # Would print: Hello \n\tWorld
```

For details on other string prefixes, see the [python 3 string literals reference docs](https://docs.python.org/3/reference/lexical_analysis.html#literals).

### String Formatting
The process of dynamically building strings based on variables and preset values. For example, lets say you are bulding a client dashboard that displays a welcome message (like the one in the example in ```string_formatting.py```). For this you might want to create a greeting that is along the lines of: 

```Hello <name> The weather today is <current_temperature> degrees. You have <email_count> new emails.```.

To do this you could do:
```python
name = "John Smith" # A dummy name
email_count = 3 # A representation of users # of new emails
current_temperature = 20.3567 # A representation of the current temperature in celsius 
greeting = f"Hello, {name} The weather today is {current_temperature} degrees. You have {email_count} new emails."
print(greeting)
```

Note that the preferred method of string formatting uses String literals. You can see examples of all 4 methods of formatting in ```string_formatting.py```.

## Usage

### Running

All of the code in the two demos require no external dependencies, they can be run by using ```python string_formatting.py``` or ```python string_literals.py```. 

## Real World Applications
String formatting has obvious real world applications in just about every application, String Literals are somewhat less immediately obvious. Besides for providing the latest format syntax ([fstrings](https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals)), they also allow you to do things like raw strings (as seen in the example above) and also [byte strings](https://www.python.org/dev/peps/pep-3112/) for things like [security modules](https://www.dlitz.net/software/pycrypto/api/current/Crypto.Cipher.AES-module.html).