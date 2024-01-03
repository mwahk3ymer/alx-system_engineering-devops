#!/usr/bin/python3
"""Returns to-do list information for a given employee ID and exports data in CSV format."""
import csv
import requests
import sys

def export_to_csv(user_id, user_name, tasks):
    """Export tasks to a CSV file."""
    filename = f"{user_id}.csv"
    fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for task in tasks:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": user_name,
                "TASK_COMPLETED_STATUS": task.get("completed", False),
                "TASK_TITLE": task.get("title", "Unknown Task"),
            })

    print(f"Data exported to {filename}")

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    print(f"Employee {user['name']} is done with tasks({len(todos)}/{len(todos)}):")

    for task in todos:
        print(f"\t{task['title']}")

    export_to_csv(user_id, user['name'], todos)
