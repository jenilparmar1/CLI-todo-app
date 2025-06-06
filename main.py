import json
import os

Filename = 'tasks.json'

def load_tasks():
    if not os.path.exists(Filename):
        return []

    with open(Filename, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(Filename, 'w') as file:
        json.dump(tasks, file, indent=2)

def add_task(task):
    tasks  = load_tasks()
    