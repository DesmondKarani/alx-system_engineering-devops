#!/usr/bin/python3
"""
Module to query the Reddit API, count occurrences of keywords in
titles of hot articles, and print counts in a specified format.
"""
import requests


def count_words(subreddit, word_list, counts={}, after=None):
    if not counts:
        # Normalize word_list to lowercase and count duplicates
        word_list = {word.lower(): 0 for word in word_list}
        counts = word_list.copy()

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'customUserAgent'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print('')
        return

    data = response.json()['data']
    posts = data['children']
    for post in posts:
        title = post['data']['title'].lower()
        for word in counts.keys():
            counts[word] += title.split().count(word)

    after = data['after']
    if after is not None:
        count_words(subreddit, word_list, counts, after)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print(f"{word}: {count}")


if __name__ == '__main__':
    # test code will be here
    pass
