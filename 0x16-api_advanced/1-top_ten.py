#!/usr/bin/python3
"""
0-main
"""
import requests


def top_ten(subreddit):
    """ xdd """

    x = 0

    response = requests.get(
        "https://www.reddit.com/r/{}/top.json".format(subreddit),
        headers={
            'User-agent': 'your bot 0.1'})

    if not response:
        print("none")
    else:
        while (x < 10):
            print(response.json().get('data').get(
                'children')[x].get('data').get('title'))
            x += 1
