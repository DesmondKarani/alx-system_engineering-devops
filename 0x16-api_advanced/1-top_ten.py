#!/usr/bin/python3
"""
Module to query the Reddit API and print the titles of the first
10 hot posts for a given subreddit.
"""
import requests
import sys


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts
    listed for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'customUserAgent'}
    params = {'limit': 10}  # Fetch only the first 10 posts
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        try:
            posts = response.json()['data']['children']
            for post in posts:
                print(post['data']['title'])
        except KeyError:
            print("None")
    else:
        print("None")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
