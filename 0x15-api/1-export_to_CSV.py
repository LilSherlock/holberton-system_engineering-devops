#!/usr/bin/python3
"""
    api
"""
from sys import argv
import csv
import requests

if __name__ == '__main__':

    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    user = user.json()
    todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))
    todo = todo.json()

    id_arg = argv[1]

    with open('{}.csv'.format(argv[1]), mode='w') as csvfile:
        employee_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for x in todo:
            employee_writer.writerow(
                [int(x['userId']), user.get('username'), x['completed'], x['title']])
