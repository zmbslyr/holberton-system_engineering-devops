#!/usr/bin/python3
"""Module to find number of subscribers to a subreddit using Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Function that uses Reddit API to find number of subscribers

    Args:
        subreddit (str): Subreddit to find number of subscribers

    Return:
        Total subscribers to subreddit
    """
    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    resp = requests.get(url, allow_redirects=False, headers=user_agent)
    if resp.status_code in (302, 404):
        return 0
    return resp.json().get('data').get('subscribers')
