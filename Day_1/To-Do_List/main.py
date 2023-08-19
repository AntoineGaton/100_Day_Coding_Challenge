import os
"""
- View tasks: See the list of tasks along with their current status.
- Mark tasks as completed: Indicate tasks as completed to track your progress.
- Delete tasks: Remove tasks from the list when they're no longer needed.
- Make app executable to be shared.
- Build GUI interface
- Convert txt to pdf
- option to send file to email or sms
"""
import os

def load_tasks_from_file():
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.read().splitlines()
    else:
        with open("tasks.txt", "w") as file:
            file.write("============================================\n")
            file.write("To-Do List Application\n")
            file.write("============================================\n")
            file.write(f"Total Tasks: {0}\n")

    return tasks

def save_task_to_file(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

def update_total_tasks(total_tasks):
    with open("tasks.txt", "r+") as file:
        lines = file.readlines()
        lines[3] = f"Total Tasks: {total_tasks}\n"
        file.seek(0)
        file.writelines(lines)

def main():
    print("============================================")
    print("To-Do List Application")
    print("============================================")

    list_of_tasks = load_tasks_from_file()
    total_tasks = len(list_of_tasks)

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task As Completed")
        print("4. Delete Task")
        print("5. Exit")
        print("============================================")

        choice = input("Select an option: ")

        match choice:
            case "1":
                task = input("Enter a task: ")
                new_task = f"[ ] {task}"
                list_of_tasks.append(new_task)
                save_task_to_file(new_task)
                total_tasks += 1
                update_total_tasks(total_tasks)
                print("Task Added Successfully...")
                input("Press Enter to continue...")
                print("============================================")

            case "2":
                print("Choice " + choice + " was picked...")
                input("Press Enter to continue...")
                print("============================================")
            case "3":
                print("Choice " + choice + " was picked...")
                input("Press Enter to continue...")
                print("============================================")
            case "4":
                print("Choice " + choice + " was picked...")
                input("Press Enter to continue...")
                print("============================================")
            case "5":
                print("Exiting...")
                print("============================================")
                break
            case _:
                print("Invalid choice. Please select a valid option.")
                print("============================================")

if __name__ == "__main__":
    main()
