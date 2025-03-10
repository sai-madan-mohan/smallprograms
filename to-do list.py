task = []

def add_task():
    task = input("Enter the task")
    task.append(task)
    print("Task added")

def view_tasks():
    if not tasks:
        print("No Tasks")
    else:
        print("Tasks:")
        for task in tasks:
            print(task)

def remove_task():
    task = input("Enter the task to remove")
    if task in tasks:
        tasks.remove(task)
        print("Task removed")
    else:
        print("Task not found")

while True:
    print("1. Add task")
    print("2.View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter choice")
    if choice ==1:
        add_task()
    elif choice ==2:
        view_tasks()
    elif choice==3:
        remove_task()
    elif choice == 4:
        break
    else:
        print("Invalid choice")