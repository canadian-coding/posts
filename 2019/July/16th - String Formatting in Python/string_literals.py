"""
Description:
    A demo of the different forms of string Literals available. SEE: https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
"""

# Raw strings; These are strings that will completely ignore special characters such as \n or \t
my_string = "Hello \n\tWorld" 
print(my_string) 
"""Would print:
Hello 
    World"""

my_string = r"Hello \n\tWorld" # Also works with R"Hello \n\tWorld"
print(my_string) # Would print: Hello \n\tWorld

# Byte strings; These take the string provided and build a bytes object.
# SEE: https://www.python.org/dev/peps/pep-3112/ For reference about byte string literals
# SEE: https://docs.python.org/3/library/stdtypes.html#bytes For referenec about byte objects
my_string = "Hello"
print(type(my_string))
my_string = b"Hello"
print(type(my_string))

"""Unicode Literals; Unicode literals are no longer necessary, 
        but some legacy code may contain them. It creates a unicode object with the string as the argument
        SEE: https://docs.python.org/3/c-api/unicode.html"""
my_string = "Hello"
print(type(my_string))
my_string = u"Hello"
print(type(my_string))

"""FStrings; Format strings can be seen in more detail in string_formatting.py. 
        But the basics are it allows you to construct strings using variables"""
name = "John Doe"
greeting = f"Hello, {name}"
print(greeting)