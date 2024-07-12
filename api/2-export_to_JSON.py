#!/usr/bin/python3
""" api project task 2 """

import json
import sys
import urllib.request

base_url = "https://jsonplaceholder.typicode.com/"


def fetch_write(employee_id):
    url = base_url + "users/{}".format(employee_id)
    with urllib.request.urlopen(url) as response:
        user_data = response.read()
    user = json.loads(user_data)
    username = user["username"]
    employee_name = user["name"]

    url = base_url + "todos?userId={}".format(employee_id)
    with urllib.request.urlopen(url) as response:
        todo_data = response.read()
    #  parse and load JSON from todos_data into todos
    todos = json.loads(todo_data)

    out = '{"{employee_id}": '
    out += '['
    notfirst = False
    for todo in todos:
        completed = todo['completed']
        title = todo['title']
        if notfirst:
            out += ','
        else:
            notfirst = True
        out += '{'
        out += f'"task": "{title}", '
        out += f'"completed": {str(completed).lower()},'
        out += f'"username": "{username}"'
        out += '}'
    out += ']}'

    #  write the out to a file named employee_id.csv
    with open(f"{employee_id}.json", "w") as f:
        f.write(out)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        for employee_id in sys.argv[1:]:
            fetch_write(int(employee_id))

    else:
        print("Please provide an employee ID as a command-line argument.")
