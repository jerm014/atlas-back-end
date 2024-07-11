#!/usr/bin/python3
""" api project task 1 """

import json
import sys
import urllib.request

base_url = "https://jsonplaceholder.typicode.com/"


if __name__ == "__main__":

    out = ""

    if len(sys.argv) > 1:
        employee_id = int(sys.argv[1])
        url = base_url + "users/{}".format(employee_id)
        with urllib.request.urlopen(url) as response:
            user_data = response.read()
        user = json.loads(user_data)
        employee_name = user["username"]

        url = base_url + "todos?userId={}".format(employee_id)
        with urllib.request.urlopen(url) as response:
            todo_data = response.read()
        #  parse and load JSON from todos_data into todos
        todos = json.loads(todo_data)

        for todo in todos:
            completed = todo['completed']
            title = todo['title']
            out += f'"{employee_id}",' + \
                f'"{employee_name}",' + \
                f'"{completed}",' + \
                f'"{title}"\n'

        #  write the out to a file named employee_id.csv
        with open(f"{employee_id}.csv", "w") as f:
            f.write(out)

    else:
        print("Please provide an employee ID as a command-line argument.")
