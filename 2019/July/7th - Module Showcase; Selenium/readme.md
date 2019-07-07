# Selenium module showcase

## Description
Selenium, and the webdriver API are used for creating user interaction based web scripts. This can be everything from automation to end-user testing, to scraping. 

## Definitions

### Selenium
A module that allows you to instantiate browser windows and control them using python.

### Webdriver
An object within the module that allows you to instantiate and interact with a browser.

## Usage

### Requirements
For this demo you will need a few things, i've outlined the requirements below and how to set them up:
1. Selenium: to get selenium you can either use ```pip install selenium``` or in the folder with this readme run ```pip install -r requirements.txt```
2. A webdriver: This demo is using the selenium webdriver API which means you need a webdriver installed and added to [PATH](https://www.itprotoday.com/cloud-computing/how-can-i-add-new-folder-my-system-path), details for the chrome webdriver used in this demo can be found [here](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.chrome.webdriver) 

### Running

After you have obtained the requirements. in this repo you can see the demo code and actually run it by running ```python login_to_youtube.py``` or ```python3 login_to_youtube.py```.

## Real World Applications
In this repo you can see a real world application, the ```login_to_youtube.py``` file does exactly what it implies, it allows you to login to a chrome window using python. 

 Another great example would be if you are using a CMS like [Drupal]() or [WordPress]() and you want to take a bunch of lines of data and input it to a website that you don't have database access to you could write a selenium scrip that:
 1. Parses and organizes the data
 2. Logs in and inputs the data in the exact same way you would, using the front end fields