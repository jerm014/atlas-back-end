#!/usr/bin/python3
""" api project task 2 """

import json
from json import decoder
import sys
import urllib.request

base_url = "https://jsonplaceholder.typicode.com/"


def fetch_write(employee_id):
    url = base_url + "users/{}".format(employee_id)
    with urllib.request.urlopen(url) as response:
        user_data = response.read()
    user = json.loads(user_data)
    username = user["username"]

    url = base_url + "todos?userId={}".format(employee_id)
    with urllib.request.urlopen(url) as response:
        todo_data = response.read()
    #  parse and load JSON from todos_data into todos
    todos = json.loads(todo_data)

    out = {}
    tasks = []
    for todo in todos:
        task = {}
        task["task"] = todo["title"]
        task["completed"] = todo["completed"]
        task["username"] = username
        tasks.append(task)
    out[employee_id] = tasks

    #  write the out to a file named employee_id.csv
    with open(f"{employee_id}.json", "w") as f:
        # write the out as json.
        json.dump(out, f)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        for employee_id in sys.argv[1:]:
            fetch_write(int(employee_id))

    else:
        print("Please provide an employee ID as a command-line argument.")
