from os import path # Used to check if file already exists
from configparser import ConfigParser # Used to serialize and deserialize config files

config = ConfigParser() # Create ConfigParser instance

if path.exists("demo.ini"): # If the file already exists
    config.read("demo.ini") # Read it
    for value in config["Application"]: # Iterate through 'application' section
        print(f"{value}: {config['Application'][value]}") # Read config settings

else: # if no file exists
    config["Application"] = {
        "Name": "Demo application",
        "Version": 1,
        "Public": True
    } # initialize a config
    with open("demo.ini", "w") as config_file:
        config.write(config_file) # Write the config object to 'demo.ini'