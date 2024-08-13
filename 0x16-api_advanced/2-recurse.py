#!/usr/bin/python3
"""function that queries the Reddit API and returns a list
containing the titles of all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    returns a list containing the titles of all hot articles
    for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None.
    """
    h = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    p = {
        "after": after,
        "count": count,
        "limit": 100
    }
    u = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    res = requests.get(u, headers=h, params=p, allow_redirects=False)
    if res.status_code == 404:
        return None

    result = res.json().get("data")
    after = result.get("after")
    count += result.get("dist")
    for foo in result.get("children"):
        hot_list.append(foo.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
