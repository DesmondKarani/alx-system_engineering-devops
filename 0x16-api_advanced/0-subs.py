#!/usr/bin/python3
"""Module to query the Reddit API and return the number
of subscribers for a given subreddit."""

import requests
import sys


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'customUserAgent'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            return response.json()['data']['subscribers']
        except KeyError:
            return 0
    else:
        return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
