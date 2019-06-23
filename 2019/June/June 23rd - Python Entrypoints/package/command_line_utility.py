"""
Description:
    An example command line utility intended to be useable in any part of the OS. Once installed\
        You should be able to run the $ <command_name> the same way as you would run $ command_line_utility.py

Example:
    $ command_name -h
"""
import argparse # Used to create an argument parser
import sys # Used to check if any arguments have been provided

def main():
    """The main function where everything lives, you need a function to point the entrypoint to so it can\
        be run. 
    """
    # Setting up Main Argument Parser
    main_parser = argparse.ArgumentParser(description="A demo of python entrypoint")
    main_parser.add_argument("-v",'--version', action='version', version='command_name V0.0.1')

    # Setting up the main subparser
    subparsers = main_parser.add_subparsers(help="This is the help command, it is called by using -h or --help")

    example_command = subparsers.add_parser('example_command',
        help='An example with some help text')

    # Print help if no argument is provided
    if len(sys.argv)==1:
        main_parser.print_help()

    args = main_parser.parse_args()