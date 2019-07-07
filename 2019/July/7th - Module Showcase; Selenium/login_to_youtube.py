"""Description:
    A demo of the selenium module, specifically the WebDriver API

Variables:
    browser (webdriver):The main browser instance used to do everything with
"""
import time # Used to add delay between pages loading
import getpass # Allows you to type password without people seeing it

from selenium import webdriver # What allows you to instantiate a chrome browser
from selenium.webdriver.common.keys import Keys # Allows you to send keys like enter and ctrl etc.
from selenium.common.exceptions import WebDriverException # Gets thrown if chrome webdriver is not set up properly

try: # Try to create a chrome browser; Note other browsers work, I just had chrome setup see here for full ist https://selenium-python.readthedocs.io/api.html
    browser = webdriver.Chrome() # Global variable often makes sense because even API calls need an instantiated browser
except WebDriverException: # Gets thrown if chrome webdriver is not set up properly
    print("Chrome Webdriver not found in path please see: https://sites.google.com/a/chromium.org/chromedriver/home for installation instructions")
    exit()

def login_to_youtube(email, password):
    """A function to automate logging into youtube.com

    Arguments:
        email(str): The account you would like to login with's email
        password(str): The account you would like to login with's password
    """
    browser.get("https://www.youtube.com/")

    browser.find_element_by_xpath("//*[@aria-label='Sign in']").click() # Find sign in button and click it

    time.sleep(3) # Adding delay while page loads; see https://selenium-python.readthedocs.io/waits.html for better way to do this
    browser.find_element_by_xpath("//*[@aria-label='Email or phone']").send_keys(email + Keys.ENTER) # type provided email into box

    time.sleep(2) # Adding delay while page loads; see https://selenium-python.readthedocs.io/waits.html for better way to do this
    browser.find_element_by_xpath("//*[@aria-label='Enter your password']").send_keys(password + Keys.ENTER) # type provided password in

if __name__ == "__main__":
    email = input("What's your email?: ")
    password = getpass.getpass("Enter your password: ")
    login_to_youtube(email, password)