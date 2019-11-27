# Configparser in python

## Description

Making application configuration standardized. Have you ever dug into a program that someone else developed and not been able to figure out where a setting is? Maybe it's in a file somewhere alongside the installation? maybe it's hardcoded? If it is in a file is it .json? .yaml file maybe?



In most cases you don't know until you already have been given the answer. The configparser library built into python seeks to solve at least the problem of various formats by creating a native python standard configuration syntax all wrapped up into a simple to use module.



## Definitions

### Config Files

Config files are files used to store and check the configuration of a program. Specifically the config files we will be talking about in this post are ones most syntactically similar to [.ini files]( https://en.wikipedia.org/wiki/INI_file ).



### Configparser

As I mentioned in the description the configparser module is a python standard library module that standardizes program configurations. It does this by creating files that are syntactically similar to  [.ini files]( https://en.wikipedia.org/wiki/INI_file ). One key difference to most other forms of configuration files is that type casting has to be done on deserialization. configparser stores and retrieves everything as strings so any casting needs to be done in application logic.



## Usage

### Running

In this repo you can see the demo code and actually run it by running ```python configparser_demo.py``` or ```python3 configparser_demo.py```.

## Real World Applications

Any application that has state that needs to be stored and accessed can make good use of the configparser module. Also since this is a standard built into python you know that anyone using python has easy access to serialization and deserialization of the files.



## Additional info

[configparser docs]( https://docs.python.org/3/library/configparser.html )