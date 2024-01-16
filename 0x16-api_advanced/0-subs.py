#!/usr/bin/python3
"""
Module to query the Reddit API and get the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Function to get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers if the subreddit is valid, 0 otherwise.
    """
    try:
        # Set a custom User-Agent to avoid errors related to Too Many Requests
        headers = {'User-Agent': 'Custom User Agent'}
        
        # Make a GET request to the Reddit API for the subreddit information
        response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response to get the number of subscribers
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            print(f"Error: {response.status_code}")
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Example usage
if __name__ == "__main__":
    # Replace 'python' with the subreddit you want to query
    subreddit_name = 'python'
    
    # Call the function with the subreddit name
    subscribers_count = number_of_subscribers(subreddit_name)
    
    # Print the result
    print(f"The subreddit '{subreddit_name}' has {subscribers_count} subscribers.")

