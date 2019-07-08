# Argparse Optional Boolean Arguments

## Description
Argparse is a well known library for writing highly extensible, and robust scripts. In this demo you will learn how to set up an optional boolean argument.

## Definitions

### argparse
A module that allows you to create robust scripts and handles much of the complexity of this in the backend. See full [python reference](https://docs.python.org/3/library/argparse.html) for the module for details

### Arguments
Arguments are special characters you specify when running a script that allow you to alter the default functionality, provide additional information, or ask the script to print information about itself such as version or help text. Most scripts include a ```-h or --help``` option to address the second example, and to get this information you would type ```python <script file> -h``` or ```python <script file> --help```

## Usage

### Running

In this repo you can see the demo code and actually run it by running ```python optional_boolean_arguments.py``` or ```python3 optional_boolean_arguments.py```.

## Real World Applications
Lets say you are building a script that gives you the information about a domain. One optional argument could be ```-e or --expiry``` when this option is used the script returns the SSL and domain expiry information.