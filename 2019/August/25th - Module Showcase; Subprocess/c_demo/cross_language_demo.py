"""This file is used to show off a real world example of creating a build
script in python and using it to build+run a C program.
NOTE: This demo assumes you have gcc installed"""

import os # Used to determine if machine is windows or unix/macOS
import subprocess # Used to run commands from python

def compile(filename, binary_filename):
    """Function to compile the provided file in gcc"""
    # Below is equivalent to running: gcc -o hello_world hello_world.c
    print(f"Creating binary: {binary_filename} From source file: {filename}\n")
    subprocess.run(["gcc", "-o", binary_filename, filename])

def run_binary(binary_filename):
    """Runs the provided binary"""
    print(f"Running binary: {binary_filename}\n")
    subprocess.run([binary_filename])

if __name__ == "__main__":
    compile("hello_world.c", "hello_world")

    if os.name =="nt": # If on windows
        run_binary("hello_world.exe")

    else: # If on unix/mac
        run_binary("hello_world")

    print("Binary run")