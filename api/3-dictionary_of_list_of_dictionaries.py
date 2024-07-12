#!/usr/bin/python3
""" api project task 3 """

import json
import sys
import urllib.request

base_url = "https://jsonplaceholder.typicode.com/"


def fetch_write():
    """ I am well aware that I should use dictionaries
    and stuff and then convert the stuff to json using
    the json library, but this way makes more sense to
    me when reading it and is faster to write for me
    because of my limited experience with the json lib-
    ary and I'm kind of in a hurry so I feel like, for
    me, this would be more real-world than taking the
    time to learn a brand new thing when you can hack
    it out and get the same result. No one is paying
    extra for pretty and perfect code, they just want
    it to work, and my employeer wanted this task done
    last week and won't stop breathing down my neck so
    what do you expect, really?"""

    with urllib.request.urlopen(base_url + "users") as response:
        employees_data = response.read()
    employees = json.loads(employees_data)
    with urllib.request.urlopen(base_url + "todos") as response:
        todo_data = response.read()
    todos = json.loads(todo_data)

    out = '{'
    not_first_employee = False

    for employee in employees:
        if not_first_employee:
            out += ', '
        else:
            not_first_employee = True

        employee_id = employee["id"]
        employee_username = employee["username"]

        out += f'"{employee_id}": '
        out += '['
        not_first_task = False
        for todo in todos:
            if todo['userId'] != employee_id:
                continue
            completed = todo['completed']
            title = todo['title']
            if not_first_task:
                out += ', '
            else:
                not_first_task = True
            out += '{'
            out += f'"task": "{title}", '
            out += f'"completed": {str(completed).lower()}, '
            out += f'"username": "{employee_username}"'
            out += '}'
        out += ']'
    out += '}'

    with open(f"todo_all_employees.json", "w") as f:
        f.write(out)


if __name__ == "__main__":
    fetch_write()
