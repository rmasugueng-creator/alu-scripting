#!/usr/bin/python3
"""Queries the Reddit API and prints titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    base = "https://www.reddit." + "com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64)"}
    params = {"limit": 10}

    response = requests.get(
        base, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data", {}).get("children", list())
    for post in posts:
        print(post.get("data", {}).get("title"))
