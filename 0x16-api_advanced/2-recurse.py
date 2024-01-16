#!/usr/bin/python3
"""
Module to recursively query the Reddit API and return a list of titles for all hot articles in a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function to query the Reddit API and accumulate titles of hot articles.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to accumulate titles of hot articles.
        after (str): The 'after' parameter for pagination.

    Returns:
        list: List containing titles of all hot articles.
    """
    try:
        # Set a custom User-Agent to avoid errors related to Too Many Requests
        headers = {'User-Agent': 'Custom User Agent'}
        
        # Prepare parameters for the Reddit API request
        params = {'limit': 100, 'after': after}
        
        # Make a GET request to the Reddit API for the subreddit's hot posts
        response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json', headers=headers, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response to get the titles of the hot posts
            data = response.json()
            posts = data['data']['children']

            # Add titles to the hot_list
            for post in posts:
                hot_list.append(post['data']['title'])

            # Check if there are more pages (pagination)
            after = data['data']['after']
            if after is not None:
                # Recursively call the function with the 'after' parameter for the next page
                recurse(subreddit, hot_list, after)
            else:
                # No more pages, return the accumulated hot_list
                return hot_list
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
