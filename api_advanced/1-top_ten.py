#!/usr/bin/python3
"""Queries the Reddit API and prints titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit." + "com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0.0 (by /u/alu)"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data", {}).get("children", list())
    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
