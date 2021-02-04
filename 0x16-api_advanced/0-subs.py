#!/usr/bin/python3
"""
0-main
"""
import requests


def number_of_subscribers(subreddit):
    """ xdd """

    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={
            'User-agent': 'your bot 0.1'})

    if not response:
        return 0

    return(response.json().get('data').get('subscribers'))
