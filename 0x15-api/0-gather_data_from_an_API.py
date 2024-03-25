#!/usr/bin/python3
'''a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress'''

import requests
import argparse


# Function to fetch user data
def fetch_user_data(user_id):
    user_response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}"
            )
    if user_response.status_code == 200:
        return user_response.json()
    else:
        return None


# Function to fetch TODO data
def fetch_todo_data(user_id):
    todos_response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
            )
    if todos_response.status_code == 200:
        return todos_response.json()
    else:
        return []  # Return an empty list if there's an error


# Main execution
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch and display
                                     TODO progress for an employee")
    parser.add_argument("employee_id", type=int, help="ID of the employee")
    args = parser.parse_args()

    user_data = fetch_user_data(args.employee_id)
    todo_data = fetch_todo_data(args.employee_id)

    if user_data and todo_data:
        completed_tasks = sum(todo['completed'] for todo in todo_data)
        total_tasks = len(todo_data)

        print(f"""Employee {user_data['name']} is done with tasks(
              {completed_tasks}/{total_tasks}):""")
        for todo in todo_data:
            if todo['completed']:
                print(f"\t{todo['title']}")
    else:
        print(f"Error: Couldn't fetch data for employee ID {args.employee_id}")
