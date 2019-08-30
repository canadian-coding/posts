"""A test to ping a hosts root URL with GET requests"""

from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    """Extends the TaskSet class; used to define user behaviours you want the
    load test to go through per user."""
    def on_start(self):
        """on_start is called when a Locust start before any task is scheduled"""
        pass

    def on_stop(self):
        """on_stop is called when the TaskSet is stopping"""
        pass

    @task(1)
    def index(self):
        """Does a GET request to the root URL of the defined host"""
        self.client.get("/")

class WebsiteUser(HttpLocust):
    """Extends the HttpLocust class; used to define user variables such as
    TaskSet(s) and wait time between tasks"""
    task_set = UserBehavior # Set each users behaviour to the defined UserBehavior class
    min_wait = 5000 # Minimum amount of time (in milliseconds) to wait between tasks
    max_wait = 9000 # Maximum amount of time (in milliseconds) to wait between tasks
