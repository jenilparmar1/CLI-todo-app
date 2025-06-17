import json
import os

Filename = 'tasks.json'

def load_tasks():
    if not os.path.exists(Filename):
        return []
    with open(Filename, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            # If the file is empty or invalid, start fresh
            return []

def save_tasks(tasks):
    with open(Filename, 'w') as file:
        json.dump(tasks, file, indent=2)

def add_task(title):
    tasks  = load_tasks()
    new_id = tasks[-1]["id"] + 1 if tasks else 1
    new_task = {
        'id' : new_id,
        'task' : title,
        'status' : 'pending'
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return print(f"Task added: #{new_id}. {title}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks added.")
    else: 
        print("Current tasks:")
        for task in tasks:
            print(f"#{task['id']}. {task['task']} \t {task['status']}")

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    if len(updated_tasks) == len(tasks):
        print(f"No task with task id #{task_id}")
    else:
        save_tasks(updated_tasks)
        print(f"Task #{task_id} deleted")

x = True
while x:
    list_tasks()
    print("\nWhat do you want to do?")
    print(f"1. Add task \n2. Delete task \n3. Exit\n")
    choice = int(input("choice: "))
    if choice == 1: 
        title = input("New task: ")
        add_task(title)
    elif choice == 2:
        task_id = int(input("Task #: "))
        delete_task(task_id)
    elif choice == 3:
        print("Tasks saved")
        x = False
    else:
        print("False input!")
        continue
