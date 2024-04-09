#!/usr/bin/python3
"""
Module to recursively query the Reddit API and return a list
of titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetches titles of all hot articles for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'customUserAgent'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params)

    if not response.ok:
        return None

    try:
        data = response.json()['data']
        children = data['children']
        for child in children:
            hot_list.append(child['data']['title'])

        after = data['after']
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except KeyError:
        return None


if __name__ == '__main__':
    pass
