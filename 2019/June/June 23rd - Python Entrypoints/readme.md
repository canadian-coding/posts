# Script entrypoint demo

## Description
Script entrypoints are useful for allowing you to write scripts that can be accessed anywhere on the machine. They are setup in the setup.py file of your python package.

## Usage
In this repo you can see the demo code and actually run it using the steps below
1. Install as a pip package using ```pip install .```
2. In your terminal type ```command_name``` (literally command_name, this is not a placeholder)
3. The help text for the command will appear, and this can be run in any folder on your computer.

Note that to uninstall the script you need to type ```pip uninstall entrypoint-demo```

## Real World Example
Lets say you are writing a utility to download a youtube video, you want this to be callable from anywhere in the OS by typing ```$ yt-downloader --url="<video URL>"```.

To do this you would have a line in your setup.py file to specify
```python
setuptools.setup(
    # Some setup info
    
    entry_points={
          'console_scripts': ['yt-downloader = package.youtube:downloader']
      },

    # More setup info
```

This can be seen in full detail with the [PyTube module](https://github.com/nficano/pytube/blob/22157bd002ffa7139e7f13e326fbeb13921fdac7/setup.py#L59)
