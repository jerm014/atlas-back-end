#!/usr/bin/python3
""" api project task 3 """

import json
import sys
import urllib.request

base_url = "https://jsonplaceholder.typicode.com/"


def fetch_write():
    """ get the stuff and do the thing """
    out = {}

    with urllib.request.urlopen(base_url + "users") as response:
        employees_data = response.read()
    employees = json.loads(employees_data)
    with urllib.request.urlopen(base_url + "todos") as response:
        todo_data = response.read()
    todos = json.loads(todo_data)

    for employee in employees:
        employee_id = employee["id"]
        employee_username = employee["username"]

        tasks = []
        for todo in todos:
            if todo['userId'] != employee_id:
                continue
            task = {}
            task['task'] = todo['title']
            task['completed'] = todo['completed']
            task['title'] = todo['title']
            task['username'] = employee_username
            tasks.append(task)
        out[employee_id] = tasks

    with open(f"todo_all_employees.json", "w") as f:
        json.dump(out, f)


def do_it_with_github():
    """ trying this task again with github typicode data """
    base_url = "https://raw.githubusercontent.com/typicode/" + \
        "jsonplaceholder/master/data.json"
    with urllib.request.urlopen(base_url) as response:
        data = response.read()
    data = json.loads(data)

    out = {}
    for user in data["users"]:
        user_id = user["id"]
        out[user_id] = []
        for task in data["todos"]:
            if task["userId"] != user_id:
                continue
            task_dict = {}
            task_dict["task"] = task["title"]
            task_dict["completed"] = task["completed"]
            task_dict["username"] = user["username"]
            out[user_id].append(task_dict)

    out = json.dumps(out, indent=4)

    with open(f"todo_all_employees.json", "w") as f:
        f.write(out)


if __name__ == "__main__":
    fetch_write()
