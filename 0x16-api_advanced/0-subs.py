#!/usr/bin/python3
"""
    A function that queries the Reddit API and returns
    the number of subscribers.
"""
from ast import If
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """
    if subreddit:
        h = {
            "user-agent": "request"
        }

        u = "https://www.reddit.com/r/{}/about.json".format(subreddit)

        res = requests.get(u, headers=h, allow_redirects=False)
        if res.status_code != 200:
            return 0
        result = res.json().get("data")
        return result.get("subscribers")
