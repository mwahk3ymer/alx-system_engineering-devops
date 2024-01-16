#!/usr/bin/python3
"""
Module to recursively query the Reddit API, parse the titles of hot articles, and print a sorted count of given keywords.
"""

import requests

def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursive function to query the Reddit API, parse titles of hot articles, and print sorted counts of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        after (str): The 'after' parameter for pagination.
        counts (dict): Dictionary to store counts of keywords.

    Returns:
        None
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

            # Process each post's title
            for post in posts:
                title = post['data']['title'].lower()  # Convert to lowercase for case-insensitivity

                # Count occurrences of keywords in the title
                for keyword in word_list:
                    keyword_lower = keyword.lower()
                    if keyword_lower in title:
                        counts[keyword_lower] = counts.get(keyword_lower, 0) + title.count(keyword_lower)

            # Check if there are more pages (pagination)
            after = data['data']['after']
            if after is not None:
                # Recursively call the function with the 'after' parameter for the next page
                count_words(subreddit, word_list, after, counts)
            else:
                # No more pages, print the sorted counts
                print_results(counts)
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

def print_results(counts):
    """
    Function to print the sorted counts of keywords.

    Args:
        counts (dict): Dictionary containing counts of keywords.

    Returns:
        None
    """
    # Sort the counts first by count (descending) and then alphabetically (ascending)
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    # Print the results
    for keyword, count in sorted_counts:
        print(f"{keyword}: {count}")
