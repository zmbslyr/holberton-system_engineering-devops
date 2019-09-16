#!/usr/bin/python3
"""Create data from an HTTP API"""
import sys
import requests

if __name__ == "__main__":
    # Request data from website
    emp = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId=" + sys.argv[1]
    )
    todo = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId=" + sys.argv[1]
    )
    # Convert requested data to JSON
    emp_dic = emp.json()
    todo_list = todo.json()
    # Save JSON data
    emp_name = emp_dic.get("name")
    num_tasks = len(todo_list)
    comp_tasks = [
        dic for dic in todo_list if dic.get("completed") is True
    ]
    # Print data in specified format
    print("Employee {} is done with tasks({}/{}):".format(
        emp_name,
        len(comp_tasks),
        num_tasks)
        )
    for task in comp_tasks:
        print("\t {}".format(task.get("title")))
