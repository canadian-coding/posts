import logging # Module that allows you to create logs; Logs are very helpful for down the road debugging
import datetime # Used in formatting strings to identify date and time

def print_num():
    """Takes user input, and if it's an int or float prints it."""
    logging.debug("Starting print_int") # Only gets logged if loggers level is DEBUG (10) or below
    try:
        logging.info("Prompting for input") # Only gets logged if loggers level is INFO (20) or below
        user_input = input("Enter a number:")
        user_input = eval(user_input) # Convert input to an int or float
    except: # If the user enters something other than an int or float
        logging.warning(f"User didn't enter a number, they entered {user_input}") # Only gets logged if loggers level is WARNING (30) or below
    logging.info(f"User entered int or float: {user_input}")
    print(f"User entered int or float: {user_input}")

if __name__ == "__main__":
    # For backwards compatability the logging module forces % formatting for predefined values
    # SEE: For a full list of variables visit: https://docs.python.org/3/library/logging.html#logrecord-attributes
    LOG_FORMAT = "{0} | %(levelname)s | %(module)s | : %(message)s".format(datetime.datetime.now().time())

    # Instantiate a logger in the simplest way possible
    logging.basicConfig(format=LOG_FORMAT, # Pass the log format defined above to the logger
    filename='example.log', # Specifying a filename automatically puts all logs in the filename path
    filemode='w', # Allows you to specify filemode; SEE: https://docs.python.org/3.7/library/functions.html#open
    level=logging.DEBUG) # Defines what type of logs should show up; SEE: https://docs.python.org/3/howto/logging.html#logging-levels
    print_num()