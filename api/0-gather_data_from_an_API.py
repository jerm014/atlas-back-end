#!/usr/bin/python3
""" api project task 0 """

import json
import sys
import urllib.request

base_url = "https://jsonplaceholder.typicode.com/"

#  Write a Python script that, using this
#  https://jsonplaceholder.typicode.com/ REST API, for a given employee ID,
#  returns information about his/her TODO list progress.

#  Requirements:

#    * You must use urllib or requests module
#    * The script must accept an integer as a parameter, which is the
#      employee ID
#    * The script must display on the standard output the employee TODO list
#      progress in this exact format:
#        * First line: Employee EMPLOYEE_NAME is done with tasks
#                      (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
#            * EMPLOYEE_NAME: name of the employee
#            * NUMBER_OF_DONE_TASKS: number of completed tasks
#            * TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the
#              sum of completed and non-completed tasks
#    * Second and N next lines display the title of completed tasks:
#      TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
#    * If an employee has no task, just display the first line:
#        * Employee EMPLOYEE_NAME has no tasks


if __name__ == "__main__":

    if len(sys.argv) > 1:
        employee_id = int(sys.argv[1])
        url = base_url + "users/{}".format(employee_id)
        with urllib.request.urlopen(url) as response:
            user_data = response.read()
        user = json.loads(user_data)
        employee_name = user["name"]

        url = base_url + "todos?userId={}".format(employee_id)
        with urllib.request.urlopen(url) as response:
            todos_data = response.read()
        #  parse and load JSON from todos_data into todos
        todos = json.loads(todos_data)

        completed = [todo["title"] for todo in todos if todo["completed"]]
        total_tasks = len(todos)
        completed_tasks_count = len(completed)

        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, completed_tasks_count, total_tasks))

        for task in completed:
            print("\t {}".format(task))
    else:
        print("Please provide an employee ID as a command-line argument.")
