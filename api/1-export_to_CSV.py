#!/usr/bin/python3
""" api project task 1 """

import csv
import json
import sys
import urllib.request


base_url = "https://jsonplaceholder.typicode.com/"


def fetch_write(empoyee_id):
    """ get the stuff and do the thing """
    url = base_url + "users/{}".format(employee_id)
    with urllib.request.urlopen(url) as response:
        user = json.loads(response.read())

    url = base_url + "todos?userId={}".format(employee_id)
    with urllib.request.urlopen(url) as response:
        todos = json.loads(response.read())

    todos_out = []
    for todo in todos:
        task = {}
        task["user_id"] = user["id"]
        task["username"] = user["username"]
        task["completed"] = todo["completed"]
        task["title"] = todo["title"]
        todos_out.append(task)

    with open(f"{user['id']}.csv", "w") as csvfile:
        fieldnames = ["user_id", "username", "completed", "title"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

        for todo in todos_out:
            writer.writerow(todo)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for employee_id in sys.argv[1:]:
            fetch_write(int(employee_id))
    else:
        print("Please provide an employee ID as a command-line argument.")
