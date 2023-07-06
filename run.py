import json


def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

    return tasks


def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)


def add_task(tasks):
    task = input("Enter task name: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")


def remove_task(tasks):
    print("Current tasks:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

    index = int(input("Enter the index of the task to remove: ")) - 1
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid index.")


def show_tasks(tasks):
    if tasks:
        print("Current tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
    else:
        print("No tasks found.")


def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager")
        print("1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            show_tasks(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using Task Manager!")

if _name_ == "_main_":
        main()
