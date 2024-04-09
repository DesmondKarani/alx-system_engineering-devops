#!/usr/bin/python3
"""Module to query the Reddit API and return the number
of subscribers for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Retrieves the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """

    headers = {'User-Agent': 'MyCustomUserAgent/1.0'}  # Customize User-Agent
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise exception for error status codes

        data = response.json()
        return data['data']['subscribers']  # Extract subscriber count

    except requests.exceptions.RequestException as error:
        print(f"Error occurred: {error}")
        return 0
