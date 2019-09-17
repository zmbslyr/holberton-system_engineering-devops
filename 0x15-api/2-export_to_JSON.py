#!/usr/bin/python3
"""Module to export API data into JSON format"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    # Request data from website
    emp = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
    )
    todo = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId=" + sys.argv[1]
    )
    # Convert requested data to JSON
    empDic = emp.json()
    todoList = todo.json()
    # Save data as JSON object to export
    taskData = []
    taskDict = {}
    jsonData = {}
    for task in todoList:
        taskDict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": empDic.get("username"),
        }
        taskData.append(taskDict)
    jsonData = {sys.argv[1]: taskData}
    # Export saved JSON object
    with open("{}.json".format(sys.argv[1]), "w") as emp:
        json.dump(jsonData, emp)
