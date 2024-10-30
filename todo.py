tasks = []

def add_task(task):
    """Adds a new task to the list"""
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    """Displays all tasks in the list"""
    if tasks:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks found.")

def delete_task(task_number):
    """Deletes a task by its number in the list"""
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' deleted.")
    else:
        print("Invalid task number.")

def show_menu():
    """Shows the menu of options"""
    print("\nTo-Do List App")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

def run():
    """Runs the main loop of the To-Do list app"""
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            task = input("Enter a new task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()
