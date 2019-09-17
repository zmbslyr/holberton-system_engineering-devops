#!/usr/bin/python3
"""Module to export and show dictionaries an JSON format"""
from collections import OrderedDict
import csv
import json
import requests
import sys


if __name__ == "__main__":
    # Request data from website
    emp = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )
    todo = requests.get(
        "https://jsonplaceholder.typicode.com/todos"
    )
    # Convert requested data to JSON
    empDic = emp.json()
    todoList = todo.json()
    # Save data to JSON format for export
    jsonData = OrderedDict()
    taskData = []
    for emp in empDic:
        for task in todoList:
            if emp.get("id") == task.get("userId"):
                taskDic = {
                    "username": emp.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                }
                taskData.append(taskDic)
        jsonData["{}".format(emp.get("id"))] = taskData
        taskData = []
    # Export data to JSON file
    with open("todo_all_employees.json", "w") as employ:
        json.dump(jsonData, employ)
