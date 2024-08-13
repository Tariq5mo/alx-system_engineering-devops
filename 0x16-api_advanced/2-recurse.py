#!/usr/bin/python3
"""function that queries the Reddit API and returns a list
containing the titles of all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    returns a list containing the titles of all hot articles
    for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None.
    """
    if after is None:
        return []

    h = {
        "user-agent": "request"
    }
    u = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    u += "?limit=100&after={}".format(after)
    res = requests.get(u, headers=h, allow_redirects=False)

    if res.status_code != 200:
        return None

    result = res.json()
    hot = result.get("data").get("children")

    for post in hot:
        hot_list.append(post.get("data").get("title"))

    return hot_list + recurse(subreddit, [], result.get("data").get("after"))
