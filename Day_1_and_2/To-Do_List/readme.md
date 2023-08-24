# To-Do List Application Documentation

This is a command-line To-Do List Application written in Python. It allows users to manage their tasks by adding, viewing, marking as completed, and deleting tasks. The application stores tasks in a file and maintains a count of total tasks.

## Usage

1. Run the script using Python 3: `python main.py`.
2. Follow the on-screen prompts to interact with the application.

## Functionality

1. **View Tasks:**
   - Choose option 1 to view the list of tasks.
   - If there are no tasks, a message will be displayed.
   - If tasks are available, they will be displayed with their current status.
   - Press Enter to continue after viewing the tasks.

2. **Add Task:**
   - Choose option 2 to add a task.
   - Enter the task description when prompted.
   - The task will be added to the list along with an unchecked checkbox.
   - The total task count will be updated in the file.

3. **Mark Task As Completed:**
   - Choose option 3 to mark a task as completed.
   - If there are no tasks, a message will be displayed.
   - If tasks are available, they will be displayed with index numbers.
   - Enter the number of the task to mark as completed.
   - The checkbox for the selected task will be updated to [X].
   - The total task count will be updated in the file.

4. **Delete Task:**
   - Choose option 4 to delete a task.
   - Enter the number of the task to delete.
   - The selected task will be removed from the list.
   - The total task count will be updated in the file.

5. **Exit:**
   - Choose option 5 to exit the application.

## File Management

- The application uses a file named "tasks.txt" to store tasks and total task count.
- If "tasks.txt" doesn't exist, it will be created with an initial total task count of 0.
- The file structure includes application title, total task count, and list of tasks.

## Usage of ANSI Escape Codes

The application uses ANSI escape codes to add color to text output. The available colors are:
- RED: Error messages
- GREEN: Successful messages
- YELLOW: Informative messages
- BLUE: Task list headers

## Recent Changes (Day 2 | 8/20/23)

- Updated the "View Tasks" functionality to display tasks as incomplete by default.
- Improved error handling for task deletion to handle invalid task numbers.
- Enhanced the task deletion process to show a message when a task is removed.
- Added the usage of ANSI escape codes to differentiate error messages and other text output.

## Note

- This application requires Python 3.10 or later.
- Press Enter to continue after each operation.

## Author

Antoine Gaton

## Date

8/20/23
