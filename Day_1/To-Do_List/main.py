"""
Things To Do Tomorrow:
- Fix mark completed bug where box is marked but the heading dissapears.
- Fix user interface.
- Center heading and add color.
- USING TKINTER FOR GUI

Things To Do In The Future:
- Mark tasks as completed: Indicate tasks as completed to track your progress.
- Delete tasks: Remove tasks from the list when they're no longer needed.
- Make app executable to be shared.
- Build GUI interface
- Convert txt to pdf
- option to send file to email or sms
- add datetime for when task was added
- add datetime for when task was completed
- remove task from list when completed after 7 days
- add option to view completed tasks
- add option to view deleted tasks
- add option to view tasks by date
- add option to view tasks by priority
- add option to view tasks by category
- add option to view tasks by status
- add settings to change theme and configure other options
- make app executable to be shared!
"""
import os
# ANSI escape codes for text color
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"

TASKS_FILE = "tasks.txt"

def load_tasks_from_file():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = file.read().splitlines()
    else:
        initialize_tasks_file()

    return tasks

def initialize_tasks_file():
    with open(TASKS_FILE, "w") as file:
        file.write("============================================\n")
        file.write("To-Do List Application\n")
        file.write("============================================\n")
        file.write("Total Tasks: 0\n")

def update_total_tasks(total_tasks):
    with open(TASKS_FILE, "r+") as file:
        lines = file.readlines()
        lines[3] = f"Total Tasks: {total_tasks}\n"
        file.seek(0)
        file.writelines(lines)

def save_tasks_to_file(tasks, total_tasks):
    with open(TASKS_FILE, "w") as file:
        file.write("============================================\n")
        file.write("To-Do List Application\n")
        file.write("============================================\n")
        file.write(f"Total Tasks: {total_tasks}\n")
        for task in tasks:
            file.write(task + "\n")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=================================================")
    print("|"+BLUE+"\t\tTo-Do List Application\t\t"+RESET+"|")
    print("=================================================")

    list_of_tasks = load_tasks_from_file()
    total_tasks = len(list_of_tasks)

    try:
        while True:
            print("|\t1. View Tasks")
            print("|\t2. Add Task")
            print("|\t3. Mark Task As Completed")
            print("|\t4. Delete Task")
            print("|\t5. Exit")
            print("=================================================")

            choice = input("Select an option: ")

            match choice:
                case "1":
                    if total_tasks == 0:
                        print("No tasks available.")
                    else:
                        for task in list_of_tasks:
                            print(task)
                    input("Press Enter to continue...")
                    os.system('cls' if os.name == 'nt' else 'clear')

                case "2":
                    task = input("Enter a task: ")
                    new_task = f"[ ] {task}"
                    list_of_tasks.append(new_task)
                    total_tasks += 1
                    update_total_tasks(total_tasks)
                    save_tasks_to_file(list_of_tasks, total_tasks)
                    print("Task Added Successfully...")
                    input("Press Enter to continue...")
                    os.system('cls' if os.name == 'nt' else 'clear')


                case "3":
                    if total_tasks == 0:
                        print("No tasks available to mark as completed.")
                    else:
                        print("Current Tasks:")
                        for idx, task in enumerate(list_of_tasks, start=1):
                            print(f"{idx}. {task}")

                        task_number = input("Enter the number of the task to mark as completed: ")

                        try:
                            task_number = int(task_number)
                            if 1 <= task_number <= total_tasks:
                                task_index = task_number - 1
                                task = list_of_tasks[task_index]
                                if task.startswith("[ ]"):
                                    list_of_tasks[task_index] = "[X]" + task[3:]
                                    update_total_tasks(total_tasks)
                                    with open("tasks.txt", "a") as file:
                                        # Append the modified task back to the file
                                        file.write(list_of_tasks[task_index] + "\n")
                                    print(f"Task '{task[3:]}' marked as completed.")
                                else:
                                    print("Task is already marked as completed.")
                            else:
                                print("Invalid task number.")
                        except ValueError:
                            print("Invalid input. Please enter a valid task number.")

                    input("Press Enter to continue...")
                    print("============================================")

                case "4":
                    task_to_delete = int(input(f'Which task would you like to delete? Valid options are 4 to {len(list_of_tasks)-1}: '))

                    while task_to_delete > len(list_of_tasks) or task_to_delete < 3:
                        print(RED+"Invalid task number. Please select a valid task number."+RESET)
                        task_to_delete = int(input("Which task would you like to delete? "))
                    
                    print(f'Removing --->{RED}{list_of_tasks[task_to_delete]}{RESET}<--- from the list...')
                    list_of_tasks.pop(task_to_delete)
                    
                    total_tasks -= 1
                    update_total_tasks(total_tasks)
                    
                    with open("tasks.txt", "w") as file:
                        file.write("============================================\n")
                        file.write("To-Do List Application\n")
                        file.write("============================================\n")
                        file.write(f"Total Tasks: {total_tasks}\n")
                        for task in list_of_tasks:
                            file.write(task + "\n")
                    input("Press Enter to continue...")
                    print("============================================")
                
                case "5":
                    print("Exiting...")
                    print("============================================")
                    break
                
                case _:
                    print("Invalid choice. Please select a valid option.")
                    print("============================================")
    
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n============================================")
        print("Exiting...")
        print("============================================")

if __name__ == "__main__":
    main()
