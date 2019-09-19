#!/usr/bin/python3
"""Module to use recursive function to query Reddit API"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=""):
    """Function to recursively return list
       containing hot post titles for a given sub

    Args:
        subreddit   (str): subreddit to query
        hot_list    (list): List of hot posts
        count       (int): Finds if any posts exist in JSON data
        after       (str): Checks the end of the URL

    Return:
        List containing all hot posts from a subreddit
    """
    user_agent = {"User-agent": "python:hbtn695:1.0"}
    url = "https://www.reddit.com/r/{}/hot.json?after={}&count={}".format(
        subreddit,
        after,
        count
    )
    resp = requests.get(url, allow_redirects=False, headers=user_agent)
    if resp.status_code in (302, 404):
        return None
    resp_json = resp.json()
    after = resp_json.get("data").get("after")
    count += resp_json.get("data").get("dist")
    if count == 0:
        return None
    for post in resp_json.get("data").get("children"):
        hot_list.append(post.get("data").get("title"))
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, count=count, after=after)
