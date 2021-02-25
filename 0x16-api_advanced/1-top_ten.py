#!/usr/bin/python3
"""
0-main
"""
import requests


def top_ten(subreddit):
    """ xdd """

    x = 0

    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={'User-agent': 'your bot 0.1'}, params={'after': after})

    if not response:
        print("None")
    else:
        while (x < 10):
            print(response.json().get('data').get(
                'children')[x].get('data').get('title'))
            x += 1
