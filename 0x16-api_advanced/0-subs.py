#!/usr/bin/env bash
"""Module to find number of subscribers to a subreddit using Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Function that uses Reddit API to find number of subscribers

    Args:
        subreddit (str): Subreddit to find number of subscribers

    Return:
        Total subscribers to subreddit
    """
    path = "https://www.reddit.com" + subreddit + "/about.json"
    header = {"User_Agent": "Mozilla/5.0"}
    print(path)
    resp = requests.get(path, headers=header, allow_redirects=False)
    if resp.status_code in (302, 404):
        return 0
    return resp.json().get("data").get("subscribers")
