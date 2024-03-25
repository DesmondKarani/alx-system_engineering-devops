#!/usr/bin/python3
'''Extend the previous script to export data in the CSV format.'''

import csv
import requests
from sys import argv


def export_tasks_to_csv(employee_id):
    """Exports an employee's tasks to a CSV file."""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
            )

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.ok and todos_response.ok:
        user = user_response.json()
        todos = todos_response.json()

        with open(f"{employee_id}.csv", 'w', newline='') as csvfile:
            taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

            for task in todos:
                taskwriter.writerow([
                    employee_id,
                    user['username'],
                    task['completed'],
                    task['title']
                ])


if __name__ == "__main__":
    if len(argv) == 2:
        try:
            employee_id = int(argv[1])
            export_tasks_to_csv(employee_id)
        except ValueError:
            print("Please provide a valid integer for the employee ID.")
    else:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
