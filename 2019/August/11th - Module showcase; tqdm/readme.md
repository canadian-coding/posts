# TQDM module showcase

## Description

tqdm is a python module that allows you to create progress bars. It works by wrapping an iterable in the tqdm object, more info can be found in the [readme](https://github.com/tqdm/tqdm/blob/master/README.rst) from the [source code](https://github.com/tqdm/tqdm)

## Definitions

### TQDM

A module that allows you to create progress bars for iterables in python.

## Usage

### Requirements

For this demo you will need a few things, i've outlined the requirements below and how to set them up:
TQDM: to get tqdm you can either use ```pip install tqdm``` or in the folder with this readme run ```pip install -r requirements.txt```

### Running

After you have obtained the requirements. in this repo you can see the demo code and actually run it by running ```python tqdm_demo.py``` or ```python3 tqdm_demo.py```.

## Real World Applications

This module is incredibly useful for scripts that have any long iteration processes. For example if you are scraping contents from an HTML table on a webpage that has a few hundred entries adding a progress bar let's users (including you) know that the script/program hasn't crashed and is just taking a while to process.
