import requests
import time


class Calculator:

    def sum(self, a, b):
        time.sleep(5)
        return a + b


class Blog:

    def __init__(self, name):
        self.name = name

    def posts(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")

        return response.json()

    def __repr__(self):
        return '<Blog: {}'.format(self.name)
