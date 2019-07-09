# CodeTags in Python

## Description
CodeTags are a way to add comments that indicate specific meanings. They are not officially supported in the python language specification, and as such are more of a convention than a feature. Still they are incredibly useful for code organization in large projects, and during collaboration.

Also some code editors (like VSCode), actually recognize CodeTags and highlight them for you to make them stand out.

## Definitions

### Code Tag
A code tag is a predefined phrase (usually in all caps) that has a specific meaning. For example TODO is a CodeTag that lets people who are reading the comment know that something needs to be done. 

The typical syntax for this is ```<CODETAG>: <Description> ``` for example:
```python
username = input("enter username: ") #TODO: Save user input after entry
```

## Usage

Since codetags are not 'officially' supported there is no full list of CodeTags (the closest is in the original proposal [PEP-350](https://www.python.org/dev/peps/pep-0350/#mnemonics))
but I have compiled a list of the most common/useful ones:
```python
# NOTE: A general note/mild warning
# HACK: Temporary solution to a problem, to be properly solved later
# PORT: An OS/Platform specific workaround
# IDEA: An idea to solve an issue (Not that useful unless solution will take time to implement)
# REQ: Requirement for a file/function/class
# FAQ: A frequently asked question
# SEE: Point to a reference such as a documentation link, or other function
# TODO: As the name implies, tells people/you something that needs to be done (very useful for multi-day/multi-developer projects)
# FIXME: Addresses a problem that should be fixed in the code
# BUG: Identifies a known bug
# WONTFIX: Put next to something you know has an unintended/unexpected outcome, but have no intention to fix
# CAVEAT: A caveat to the implementation; something that is not so obvious to layman's, or first time users necessarily
# DOCUMENT:Need to write documentation
```
### Running

There isn't really a demo for this, since it is documentation related. I have included some random functions in ```codetags.py``` that include various CodeTags as examples of the functionality. 

## Real World Applications
These CodeTags can be a real help for quickly identifying tasks that need to be done, especially when using CodeTags that have syntax highlighting such as NOTE, TODO, HACK, BUG, and FIXME.

KEEP IN MIND, I am not suggesting you actually use all of these in every situation. You will notice the example is very obnoxious with it's use of CodeTags, this is for demo purposes only, realistically these tend to be used every so often (AKA don't piss off your whole team littering your entire codebase with CodeTags every line or two).