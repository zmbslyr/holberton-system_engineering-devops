#!/usr/bin/python3
"""Module to find top ten hot posts using Reddit API"""
import requests


def top_ten(subreddit):
    """print titles of first 10 hot posts listed for a given sub
    
    Args:
        subreddit (str): subreddit to find top ten hot posts in

    Return:
        Top ten hot posts
    """
    user_agent = {'User-agent': 'Mozilla/5.0'}
    path = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    resp = requests.get(path, allow_redirects=False, headers=user_agent)
    if resp.status_code in (302, 404):
        print(None)
    else:
        for post in resp.json().get('data').get('children'):
            print(post.get('data').get('title'))
