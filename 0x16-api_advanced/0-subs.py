#!/usr/bin/python3
""" Write a function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers) for a
given subreddit. If an invalid subreddit is given, the function
should return 0. """

import requests


def number_of_subscribers(subreddit):
    """Write a function that queries the Reddit API"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url)
    try:
        return req.json().get("data").get("subscribers")
    except Exception:
        return 0
