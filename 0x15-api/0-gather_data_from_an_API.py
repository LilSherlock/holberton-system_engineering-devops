#!/usr/bin/python3
"""
    api
"""
import sys
import requests


if __name__ == '__main__':

    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    user = user.json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo = todo.json()

    id_arg = int(sys.argv[1])
    tasks = 0

    for x in todo:
        if x['userId'] == id_arg and x['completed']:
            tasks += 1

    print("Employee {} is done with tasks({}/20):".format(user.get("name"), tasks))
    for x in todo:
        if x['userId'] == id_arg and x['completed']:
            print("\t {}".format(x['title']))
