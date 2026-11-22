#!/usr/bin/python3
"""Recursively queries the Reddit API and returns all hot article titles."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Returns a list of titles of all hot posts for a given subreddit."""
    if hot_list is None:
        hot_list = list()

    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit." + "com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0.0 (by /u/alu)"}
    params = {"after": after, "limit": 100}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    posts = data.get("children", list())
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")
    if after is not None:
        return recurse(subreddit, hot_list, after)

    return hot_list
