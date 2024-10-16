tasks = []

def displaymenu():
    print("To-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def addtask():
    new_task = input("Enter a new task: ")
    tasks.append(new_task)
    print(f"Task '{new_task}' added.")

def viewtasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def deletetask():
    viewtasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        displaymenu()
        choice = input("Choose an option: ")
        if choice == '1':
            addtask()
        elif choice == '2':
            viewtasks()
        elif choice == '3':
            deletetask()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
            