""" Subprocess is a module that lets you run commands and executable files
from a python script."""
import os # Used to determine OS and run cls/clear commands
import subprocess # Used to run external commands/executable files

# Clears terminal after starting file: this helps with legibility
if os.name == "nt":# PORT: If on windows then run the cls command
    os.system("cls")
else: # PORT: If on unix/mac then run the clear comand
    os.system("clear") 

print("This is running in the subprocess_demo.py file\n")

# Run the test script for respective OS's
if os.name == "nt": # PORT: If on windows then run the .bat version
    print("Starting up test_script.bat\n\n")
    subprocess.run(["test_script.bat"])

else: # PORT: If on unix/mac then run the .sh version
    print("Starting up test_script.sh\n\n")
    subprocess.run(["test_script.sh"])