"""A demo of optional boolean arguments using argparse."""
import argparse # Module used to set up argument parser

# Setting up Main Argument Parser
main_parser = argparse.ArgumentParser(description="A demo of optional boolean arguments")

# Adding optional boolean argument
main_parser.add_argument("-r", '--run',
help="If argument is present run 'print('hello')'",
action='store_true', # If -r is present, the argument is True
default=False, # If -r is not present the argument is False
required=False, # Makes argument optional
dest="run") # Makes variable accessible as 'run', see lines 19-26

def function_to_run():
    """Function intended to run if the -r or --run command is used"""
    print("-r or --run was called")

# Argument parsing
args = main_parser.parse_args()

if args.run: # If -r or --run is specified, run function_to_run()
    function_to_run()

else: # If -r or --run was not present
    print("-r or --run was not called")
