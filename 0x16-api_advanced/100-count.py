#!/usr/bin/python3
"""
Count words in all hot posts from a given Reddit.
"""
import requests
import sys


def count_words(subreddit, word_list, after=None, counts={}):
    """ recursive function that queries the Reddit API,
 parses the title of all hot articles,
 and prints a sorted count of given keywords
 (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not).
    """
    if not word_list or word_list == [] or not subreddit:
        return

    u = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    h = {"User-Agent": "Mozilla/10.0/API"}

    p = {"limit": 100}

    if after:
        p["after"] = after

    res = requests.get(u, headers=h, params=p, allow_redirects=False)

    if res.status_code != 200:
        return

    MainData = res.json()

    data = MainData.get("data")

    children = data.get("children")

    for po in children:
        title_of = po.get("data", {}).get("title").lower()

        for w in word_list:
            if w.lower() in title_of:
                counts[w] = counts.get(w, 0) + title_of.count(w.lower())

    after = MainData.get("data", {}).get("after")

    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sort = sorted(counts.items(), key=lambda x: (-x[1], x[0].lower()))

        for w, count in sort:
            print(f"{w.lower()}: {count}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
