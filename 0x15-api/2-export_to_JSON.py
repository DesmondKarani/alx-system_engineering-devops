#!/usr/bin/python3
'''Extend the previous script to export data in the JSON format.'''

import json
import requests
from sys import argv


def export_tasks_to_json(employee_id):
    """Exports an employee's tasks to a JSON file."""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
            )

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.ok and todos_response.ok:
        user = user_response.json()
        todos = todos_response.json()

        tasks_list = []
        for task in todos:
            tasks_list.append({
                "task": task['title'],
                "completed": task['completed'],
                "username": user['username']
            })

        tasks_dict = {str(employee_id): tasks_list}

        with open(f"{employee_id}.json", 'w') as jsonfile:
            json.dump(tasks_dict, jsonfile)


if __name__ == "__main__":
    if len(argv) == 2:
        try:
            employee_id = int(argv[1])
            export_tasks_to_json(employee_id)
        except ValueError:
            print("Please provide a valid integer for the employee ID.")
    else:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
