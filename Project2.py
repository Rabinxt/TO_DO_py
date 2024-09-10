
# Simple To-Do List Application: Conceptual Breakdown
# Goal:
# The objective is to build a to-do list application where users can:

# Add tasks.
# Delete tasks.
# Mark tasks as complete.
# Save their to-do list to a file and retrieve it later.
# Key Concepts:
# Class Structure: You’ll need to define a class called Task to represent individual tasks. Each task will have the following attributes:

# Name: The description of the task (e.g., "Buy groceries").
# Status: The state of the task (e.g., "Complete" or "Incomplete").
# Operations on the To-Do List: You’ll store multiple tasks in a list, and the program will allow users to perform various operations:

# Adding Tasks: Users will be able to create a new task by providing a name, and the status will be set to "Incomplete" by default. This task will be added to the list.

# Deleting Tasks: Users will select a task to delete. The program will remove the corresponding task from the list.

# Marking as Complete: Users can choose a task from the list and mark it as "Complete". This will update the status of the task.

# Displaying Tasks: The program will display all tasks, showing their name and status, so users can see what’s pending or completed.

# File Handling: The to-do list will be saved to a file, allowing users to retrieve their tasks even after restarting the program. This introduces the concept of file handling:

# Saving the List: After each operation (adding, deleting, or marking tasks), the program will save the entire task list to a file (e.g., todo_list.txt). Each task’s name and status will be written to the file.

# Loading the List: When the program starts, it will read the file and load all previously saved tasks. This allows the user to pick up where they left off.

# User Interface (Text-Based): The application will be a simple, text-based interface where users are prompted to:

# Enter new tasks.
# Choose tasks to delete or mark as complete.
# View the current list of tasks.
# The user will interact with the program through menu-driven options (e.g., "Press 1 to add a task", "Press 2 to delete a task", etc.).

class to_do:
    def __init__(self,number,name,status="pending"):
        self.number=number
        self.name=name
        self.status=status

    def add(self,number, task_name):
        with open("list.txt", "a") as text_file:
            text_file.write(f"{number}{task_name},pending\n")
    
    def delete(self , number):
        with open("list.txt","r") as text_file:
            tasks = text_file.readlines()
        with open("list.txt","w") as text_file:
            found=False
            for task in tasks:
                task_data=task.split(",")
                if task_data[0] != number:
                    text_file.write(task)
                else:
                    found=True
                if found:
                    print(f"Task with number {number} deleted sucessfully")
                else:
                    print(f"Task with number {number} not found. ")

    def complete(self):
        self.status = "marked"

    def display_task(self):
        with open("list.txt","r") as text_file:
            tasks = text_file.read()
            print(tasks)
#  Create an instance of the ToDo class
Task = to_do("1","task1")

# Menu-driven interface with correct input handling
while True:
    task_numbers = input(
        "Press 1 to Add task\nPress 2 to Delete the task\nPress 3 to Mark complete\nPress 0 to Display tasks\nPress any other key to Exit\nAns: ")

    if task_numbers == "1":
        inf_num = input("Enter the task number: ")
        inf_name = input("Enter the task name: ")
        Task.add(inf_num, inf_name)
        Task.display_task()


    elif task_numbers == "2":
        inf_num = input("Enter the task number to delete: ")
        Task.delete(inf_num)
        Task.display_task()


    elif task_numbers == "3":
        inf_num = input("Enter the task number to mark as complete: ")
        Task.complete(inf_num)
        Task.display_task()


    elif task_numbers == "0":
        Task.display_task()

    else:
        print("Exiting the program.")
        break