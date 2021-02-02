#!/usr/bin/python3
"""Exports data in the CSV format"""
from sys import argv
import requests
import json

if __name__ == '__main__':

    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    user = user.json()
    todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))
    todo = todo.json()

    xd = []
    for x in todo:

        todo_dict = {}
        todo_dict["task"] = x.get("title")
        todo_dict["completed"] = x.get('completed')
        todo_dict["username"] = user.get('username')
        xd.append(todo_dict)

    json_dict = {}
    json_dict[argv[1]] = xd

    with open("{}.json".format(argv[1]), 'w') as json_file:
        json.dump(json_dict, json_file)
