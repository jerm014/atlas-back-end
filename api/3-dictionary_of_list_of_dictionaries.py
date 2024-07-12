#!/usr/bin/python3
""" api project task 3 """

import json
import sys
import urllib.request

base_url = "https://jsonplaceholder.typicode.com/"


def fetch_write():
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

    #  write the out to a file named employee_id.csv
    with open(f"todo_all_employees.json", "w") as f:
        f.write(out)


if __name__ == "__main__":
    fetch_write()
