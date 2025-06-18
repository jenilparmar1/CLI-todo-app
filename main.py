import json
import os
from tabulate import tabulate
from colorama import Fore,  Style, init
from datetime import datetime

init(autoreset=True)
Filename = 'tasks.json'

def load_tasks():   #loads task from json file to a list
    if not os.path.exists(Filename):
        return []
    with open(Filename, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            # If the file is empty or invalid, start fresh
            return []

def save_tasks(tasks):  #saves tasks to json file 
    with open(Filename, 'w') as file:
        json.dump(tasks, file, indent=2)

def reindex_tasks(tasks):   #restructures the json file to reindex the tasks after updates and deletes
    for index, task in enumerate(tasks, start=1):
        task["id"] = index
    return tasks

def add_task():
    title = input("New task: ")
    tasks  = load_tasks()

    new_id = tasks[-1]["id"] + 1 if tasks else 1
    now  = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")    #current time
    new_task = {
        'id' : new_id,
        'task' : title,
        'status' : 'Pending',
        "created at" : now,
        "last updated" : now
    }
    tasks.append(new_task)
    tasks = reindex_tasks(tasks)    
    save_tasks(tasks)
    return print(f"Task added: #{new_id}. {title}")

def get_colored_status(status): #colors the status based on the current status
    status_lower = status.lower()
    if status_lower == "pending":
        return Fore.RED + status + Style.RESET_ALL
    elif status_lower == "in-progress":
        return Fore.YELLOW + status + Style.RESET_ALL
    elif status_lower == "done":
        return Fore.GREEN + status + Style.RESET_ALL
    else:
        return status  # default color

def time_ago(timestamp_str):
    try:
        timestamp = datetime.strptime(timestamp_str, "%d/%m/%Y, %H:%M:%S")
    except ValueError:
        return "Unknown time"
    
    now = datetime.now()
    diff = now - timestamp  #finds difference between the current time and the timestamp

    seconds = diff.total_seconds()
    minutes = int(seconds // 60)
    hours = int(minutes // 60)
    days = int(hours // 24)

    if seconds < 60:
        return "just now"
    elif minutes < 60:
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    elif hours < 24:
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    else:
        return f"{days} day{'s' if days != 1 else ''} ago"

def list_tasks(filter_status=None):
    tasks = load_tasks()

    if filter_status:
        if filter_status == 1:
            filter_status = "pending"
        elif filter_status == 2:
            filter_status = "in-progress"
        elif filter_status == 3:
            filter_status = "done"
        else: 
            print("Invalid input")
            return
        tasks = [task for task in tasks if task["status"].lower() == filter_status] #creates list with the filtered tasks

    if not tasks:
        print("No tasks added.")
    else: 
        print("Current tasks:")
        headers = ["ID", "Task", "Status", "Created ON", "Updated ON"]
        rows = [[Fore.BLUE + str(task["id"]) + Style.RESET_ALL, Fore.LIGHTMAGENTA_EX + str(task["task"]) + Style.RESET_ALL, get_colored_status(task["status"]), Fore.GREEN + str(time_ago(task["created at"])) + Style.RESET_ALL, Fore.GREEN + str(time_ago(task["last updated"])) + Style.RESET_ALL] for task in tasks]
        print(tabulate(rows, headers=headers, tablefmt="rounded_grid")) #creates table of current tasks in json file

def delete_task():
    task_id = int(input("Task #: "))
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]   #creates list without the task with "task_id" task
    if len(updated_tasks) == len(tasks):
        print(f"No task with task id #{task_id}")
    else:
        updated_tasks = reindex_tasks(updated_tasks)
        save_tasks(updated_tasks)
        print(f"Task #{task_id} deleted")

def edit_task():
    task_id = int(input("Task #: "))    #input to identify the task
    tasks = load_tasks()
    found = False

    for task in tasks:
        if task["id"] == task_id:
            title = input("New task: ") #input for the new title of the task
            task["task"] = title
            task["last_updated"] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            found = True
            break

    if found:
        save_tasks(tasks)
        print(f"Task #{task_id} changed to {title}")
    else:
        print(f"No task found with id #{task_id}")

def edit_status():  #edits status of the task with "task_id"
    task_id = int(input("Task #: "))
    tasks = load_tasks()
    found = False

    for task in tasks:
        if task["id"] == task_id:
            print(f"\n1. Pending\n2. In-progress\n3. Done")
            while True:
                status = int(input("New status: "))
                if status == 1:
                    task["status"] = "Pending"
                    break
                elif status == 2:
                    task["status"] = "In-progress"
                    break
                elif status == 3:
                    task["status"] = "Done"
                    break
                else:
                    print("Invalid input")
            found = True
    
    if found:
        task["last updated"] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        save_tasks(tasks)
        print(f"Updated task #{task_id} status to {task["status"]}")
    else: 
        print(f"No task #{task_id} found")


x = True
while x:
    list_tasks()
    print("\nWhat do you want to do?")
    print(f"1. Add task \n2. Delete task \n3. Edit status\n4. Edit task\n5. Show tasks by Status\n6. Exit\n")
    choice = int(input("choice: "))
    if choice == 1: 
        add_task()
    elif choice == 2:
        delete_task()
    elif choice == 3:
        edit_status()
    elif choice == 4:
        edit_task()
    elif choice == 5:
        print(f"\n1. Pending\n2. In-progress\n3. Done")
        filter = int(input("Filter: "))
        list_tasks(filter_status= filter)
    elif choice == 6:
        print("Tasks saved")
        x = False
    else:
        print("False input!")
        continue
