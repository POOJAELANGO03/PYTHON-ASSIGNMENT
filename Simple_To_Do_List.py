tasks = []

def display_options():
    print("\nOptions:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    if task not in tasks:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task Already Exists")

def remove_task():
    if not tasks:
        print("No tasks to remove.")
        return
    print("Current Tasks:", tasks)
    task = input("Enter the task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' is removed!")
    else:
        print("Task not found")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:", tasks)

def exit_program():
    print("Program Exited!")

def main():
    while True:
        display_options()
        try:
            choice = input("Enter your choice: ")

            if choice == '1':
                add_task()
            elif choice == '2':
                remove_task()
            elif choice == '3':
                view_tasks()
            elif choice == '4':
                exit_program()
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()