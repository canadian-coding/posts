# Basic Logging in python

## Description

Logging is the act of generating logs from a program. These are typically stored in a file or sent to a terminal to give developers a good idea of what's going on in their program at any given time.

## Definitions

### Logging

Logging is the act of generating logs from a program. The [logging module](https://docs.python.org/3/howto/logging.html) is the standard way of doing this in python.

You can see in the example below the simplest way of setting up a logger to log to ```example.log```:

```python
import logging # Module that allows you to create logs

logging.basicConfig(filename='example.log', # Specifying a filename automatically puts all logs in the filename path
    filemode='w', # Allows you to specify filemode; SEE: https://docs.python.org/3.7/library/functions.html#open
    level=logging.DEBUG) # Defines what type of logs should show up; SEE: https://docs.python.org/3/howto/logging.html#logging-levels
logging.info("Hello World!")
```

## Usage

### Running

In this repo you can see the demo code and actually run it by running ```python logging_demo.py``` or ```python3 logging_demo.py```.

## Real World Applications

Logging is incredibly useful for debugging down the road, especially if you are running a very complicated app with many modules and files as hand debugging becomes genuinely impossible sometimes. It also helps you to understand what went wrong in edge cases when end users don't necessarily remember exactly what they did to break something.

## Additional info

[Logging in multiple modules](https://docs.python.org/3/howto/logging-cookbook.html#using-logging-in-multiple-modules)
[Logging Levels](https://docs.python.org/3/howto/logging.html#logging-levels)
[Handlers](https://docs.python.org/3/howto/logging.html#useful-handlers)
