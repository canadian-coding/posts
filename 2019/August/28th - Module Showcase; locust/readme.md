# Module Showcase; locust

## Description

Locust is a python based load testing framework, it is incredibly useful to do load testing before an application launch to ensure stability for your users once many of them get into an application.

## Definitions

### Load Testing

Load testing is faking user interactions in a web app to see how the system handles large groups of users.

### Locust

Locust is a user load testing framework built in python. It allows you to create task queues (i.e. log in, write an article, log out), set spawn and max user rates, and provide analytics to tell you how many users failed and or how much the system slowed down while all the 'users' were executing their task queues.

## Usage

### Dependencies

First you will need to install all dependencies this can be done by running either ```pip install -r requirements.txt``` or ```pip3 install -r requirements.txt```.

### Running

In this repository there is a demo that can be run with a few steps:

1. Start the demo site using ```python demo_site.py``` or ```python3 demo_site.py```
2. Run locust ```locust -f locust_demo.py --host=http://localhost:5000```; The -f is to specify your configuration file, and the host is the starting URL of the site.
3. Locust will give you a port you can access the frontend through (i.e. localhost:8089) and from there you can choose how many users to create, and set a spawn rate.

## Real World Applications

Load testing is an integral part of setting up an application to make sure it can handle at least as many expected users as you have. It also allows you to test things like DOS (denial of service) protection, and make sure your app (or even your server hardware) doesn't fall apart if there is a sudden spike.

## Additional info

[Locust Documentation](https://locust.io/)

[Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/)
