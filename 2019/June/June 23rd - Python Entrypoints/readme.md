# Script entrypoint demo
Script entrypoints are useful for allowing you to write scripts that can be accessed anywhere.

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