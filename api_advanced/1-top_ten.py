#!/usr/bin/python3
"""Queries the Reddit API and prints titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://old.reddit." + "com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
    }
    params = {"limit": 10}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data", {}).get("children", list())
    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get("data", {}).get("title"))
