#!/usr/bin/python3
"""Recursively queries the Reddit API and counts keyword occurrences."""
import requests


def count_words(subreddit, word_list, after=None, counts=None, weights=None):
    """Prints a sorted count of given keywords in hot article titles."""
    if subreddit is None or not isinstance(subreddit, str):
        return

    if counts is None:
        counts = {}
        weights = {}
        for word in word_list:
            w = word.lower()
            counts[w] = 0
            weights[w] = weights.get(w, 0) + 1

    url = "https://www.reddit." + "com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0.0 (by /u/alu)"}
    params = {"after": after, "limit": 100}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", list())
    for post in posts:
        title_words = post.get("data", {}).get("title", "").lower().split()
        for word in title_words:
            if word in counts:
                counts[word] += weights.get(word, 1)

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts, weights)

    sorted_counts = sorted(
        counts.items(), key=lambda item: (-item[1], item[0])
    )
    for word, total in sorted_counts:
        if total > 0:
            print("{}: {}".format(word, total))
