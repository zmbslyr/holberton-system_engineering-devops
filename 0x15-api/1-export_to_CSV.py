#!/usr/bin/python3
"""Module to convert API data to .csv format"""
import sys
import requests
import csv


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
    # Export data to .csv format
    with open("{}.csv".format(sys.argv[1]), "w") as expt:
        exptWrite = csv.writer(
            expt,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_ALL
        )
        for dic in todoList:
            exptWrite.writerow([
                empDic.get("id"),
                empDic.get("username"),
                dic.get("completed"),
                dic.get("title")
            ])
