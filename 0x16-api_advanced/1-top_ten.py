#!/usr/bin/python3
"""
Module to query the Reddit API and print the titles of the first 10 hot posts for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Function to print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    try:
        # Set a custom User-Agent to avoid errors related to Too Many Requests
        headers = {'User-Agent': 'Custom User Agent'}
        
        # Make a GET request to the Reddit API for the subreddit's hot posts
        response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json', headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response to get the titles of the first 10 hot posts
            data = response.json()
            posts = data['data']['children'][:10]

            # Print the titles of the posts
            print(f"Top 10 hot posts in '{subreddit}':")
            for post in posts:
                print(post['data']['title'])
        else:
            print(f"None")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace 'python' with the subreddit you want to query
    subreddit_name = 'python'
    
    # Call the function with the subreddit name
    top_ten(subreddit_name)
