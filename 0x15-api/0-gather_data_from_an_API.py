#!/usr/bin/python3
'''a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress'''

import requests
from sys import argv


def fetch_todo_list(employee_id):
    """Fetches and displays the TODO list progress for a given employee ID."""
    # Base URL for user and todo information
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = (
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
            )

    # Fetch the user information
    user_response = requests.get(user_url)
    todos_response = requests.get(todo_url)

    # Verify successful responses
    if user_response.ok and todos_response.ok:
        user = user_response.json()
        todos = todos_response.json()

        # Calculate task progress
        total_tasks = len(todos)
        completed_tasks = sum(task['completed'] for task in todos)

        # Display the progress
        print("Employee {} is done with tasks({}/{}):".format(
            user['name'], completed_tasks, total_tasks))

        # Display titles of completed tasks
        for task in todos:
            if task['completed']:
                print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(argv) == 2:
        try:
            employee_id = int(argv[1])
            fetch_todo_list(employee_id)
        except ValueError:
            print("Please provide a valid integer for the employee ID.")
    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
