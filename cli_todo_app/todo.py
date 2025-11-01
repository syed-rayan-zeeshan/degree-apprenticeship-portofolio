# Simple To-Do List App

# You can add, view, and delete tasks

# Made with Python :)

# Made by Syed Rayan Zeeshan

tasks = []  # list to store all tasks



# show menu to the user

def show_menu():

    print("\n==== TO-DO LIST MENU ====")

    print("1. View all tasks")

    print("2. Add a new task")

    print("3. Delete a task")

    print("4. Exit")



# show all tasks

def view_tasks():

    if len(tasks) == 0:

        print("No tasks yet. Try adding one!")

    else:

        print("\nYour current tasks:")

        for index in range(len(tasks)):

            print(f"{index + 1}. {tasks[index]}")



# add a new task

def add_task():

    new_task = input("Enter your new task: ")

    tasks.append(new_task)

    print(f"Task added: {new_task}")



# delete a task

def delete_task():

    view_tasks()

    if len(tasks) == 0:

        return

    try:

        task_number = int(input("Enter the task number to delete: "))

        if task_number > 0 and task_number <= len(tasks):

            deleted = tasks.pop(task_number - 1)

            print(f"Task deleted: {deleted}")

        else:

            print("That number doesn’t match any task.")

    except ValueError:

        print("Please type a number, not text.")



# main loop that runs until user quits

while True:

    show_menu()

    choice = input("Choose an option (1-4): ")



    if choice == "1":

        view_tasks()

    elif choice == "2":

        add_task()

    elif choice == "3":

        delete_task()

    elif choice == "4":

        print("Goodbye! Thanks for using the app.")

        break

    else:

        print("Invalid choice. Please pick 1, 2, 3 or 4.")

