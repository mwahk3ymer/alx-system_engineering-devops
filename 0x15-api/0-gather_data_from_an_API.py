#!/usr/bin/python3
"""
Script to fetch and display TODO list progress for a given employee ID.
"""

import requests
import sys


def get_employee_info(employee_id):
    """
    Fetch employee information and TODO list progress from the REST API.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/employees/{employee_id}"
    todos_url = f"{base_url}/todos?employee_id={employee_id}"

    # Fetch employee information
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data.get("name", "Unknown Employee")

    # Fetch TODO list for the employee
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    return employee_name, todos_data


def display_todo_progress(employee_name, todos_data):
    """
    Display TODO list progress in the specified format.
    """
    total_tasks = len(todos_data)
    completed_tasks = [
            task for task in todos_data if task.get("completed", False)
            ]

    print(f"Employee {employee_name} is done ({len(completed_tasks)}/"
        f"{total_tasks}):")

    for task in completed_tasks:
        task_title = task.get("title", "Unknown Task")
        print(f"\t{task_title}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    try:
        employee_name, todos_data = get_employee_info(employee_id)
        display_todo_progress(employee_name, todos_data)
    except requests.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
