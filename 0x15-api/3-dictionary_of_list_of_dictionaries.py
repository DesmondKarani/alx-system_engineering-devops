#!/usr/bin/python3
"""Extend the script to export data of all employees'
tasks in the JSON format."""

import json
import requests


def export_all_tasks_to_json():
    """Exports tasks of all employees to a JSON file."""
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    if users_response.ok and todos_response.ok:
        users = users_response.json()
        todos = todos_response.json()

        all_tasks = {}
        for user in users:
            user_tasks = []
            for task in todos:
                if task['userId'] == user['id']:
                    user_tasks.append({
                        "username": user['username'],
                        "task": task['title'],
                        "completed": task['completed']
                    })
            all_tasks[str(user['id'])] = user_tasks

        with open("todo_all_employees.json", 'w') as jsonfile:
            json.dump(all_tasks, jsonfile)


if __name__ == "__main__":
    export_all_tasks_to_json()
