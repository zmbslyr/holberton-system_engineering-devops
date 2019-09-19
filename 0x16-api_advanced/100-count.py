#!/usr/bin/python3
"""Module to find frequency of key words in hot post"""
import collections
import json
import urllib.parse
import requests
import io


def count_words(subreddit, word_list, hot_list=[], after=None):
    """Function to find frequency of given keywords

    Args:
        subreddit   (str): Subreddit to search
        word_list   (list): Keywords to find the frequency of
        hot_list    (list): List of hot post in subreddit
        after       (str): Adds to url if needed

    Return:
        Frequency of keywords used
    """
    path = "https://www.reddit.com"
    path += "/r/" + urllib.parse.quote(subreddit, safe="") + "/hot.json"
    path += "?raw_json=1"
    if after is not None:
        path += "&after=" + urllib.parse.quote_plus(after)
        path += "&count=" + str(len(hot_list))
    headers = {
        "Connection": "keep-alive",
        "User-Agent": "python:hbtn695:1"
    }
    resp = requests.get(path, headers=headers, allow_redirects=False)
    if resp.status_code != 200:
        return
    post = resp.json()
    hot_list.extend(p["data"]["title"] for p in post["data"]["children"])
    after = post["data"]["after"]
    if after is None:
        word_list = collections.Counter(word_list)
        count = collections.Counter(
            word
            for title in hot_list for word in title.lower().split()
        )
        print("\n".join(
            "{}: {}".format(word, count)
            for word, count in sorted((
                (word, count[word.lower()] * words)
                for word, words in word_list.items()
                if count[word.lower()] > 0
            ), key=lambda pair: (-pair[1], pair[0]))
        ))
        return
    return count_words(subreddit, word_list, hot_list, after)
