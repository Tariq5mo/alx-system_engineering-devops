#!/usr/bin/python3
""" function that queries the Reddit API and prints the titles hot posts. """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    p = {
        "limit": 10
    }

    u = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    h = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    res = requests.get(u, params=p, headers=h, allow_redirects=False)
    if res.status_code != 200:
        print("None")
        return
    result = res.json().get("data")
    [print(foo.get("data").get("title")) for foo in result.get("children")]
