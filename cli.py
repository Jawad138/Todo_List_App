import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def remove_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)
        print("Task removed successfully!")
    else:
        print("Invalid task index!")

def display_tasks():
    tasks = load_tasks()
    if tasks:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
    else:
        print("No tasks found.")

def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            display_tasks()
            index = int(input("Enter the task number to remove: ")) - 1
            remove_task(index)
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()