tasks = []

def show_tasks():
    if not tasks:
        print("\n📋 No tasks available!")
    else:
        print("\n📝 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("\n➕ Enter a new task: ")
    tasks.append(task)
    print("✅ Task added!")

def remove_task():
    show_tasks()
    try:
        task_num = int(input("\n❌ Enter task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed = tasks.pop(task_num)
            print(f"🗑️ Removed task: {removed}")
        else:
            print("⚠️ Invalid task number!")
    except ValueError:
        print("⚠️ Please enter a valid number!")

while True:
    print("\n📌 To-Do List Manager")
    print("1️⃣ View Tasks\n2️⃣ Add Task\n3️⃣ Remove Task\n4️⃣ Exit")
    choice = input("Select an option (1-4): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("👋 Exiting... Have a productive day!")
        break
    else:
        print("⚠️ Invalid choice! Please enter 1-4.")

