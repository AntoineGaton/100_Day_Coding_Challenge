# To-Do List Application Documentation

This is a command-line To-Do List Application written in Python. It allows users to manage their tasks by adding, viewing, marking as completed, and deleting tasks. The application stores tasks in a file and maintains a count of total tasks.

## Usage

1. Run the script using Python 3: `python main.py`.
2. Follow the on-screen prompts to interact with the application.

## Functionality

1. **Add Task:**
   - Choose option 1 to add a task.
   - Enter the task description when prompted.
   - The task will be added to the list along with an unchecked checkbox.
   - The total task count will be updated in the file.

2. **View Tasks:**
   - Choose option 2 to view the list of tasks.
   - The list will display tasks with their current status and index numbers.
   - Press Enter to continue after viewing the tasks.

3. **Mark Task As Completed:**
   - Choose option 3 to mark a task as completed.
   - The list of tasks will be displayed along with index numbers.
   - Enter the index of the task you want to mark as completed.
   - The checkbox for the selected task will be updated to [x].
   - The total task count will be updated in the file.

4. **Delete Task:**
   - Choose option 4 to delete a task.
   - The list of tasks will be displayed along with index numbers.
   - Enter the index of the task you want to delete.
   - The selected task will be removed from the list.
   - The total task count will be updated in the file.

5. **Exit:**
   - Choose option 5 to exit the application.

## File Management

- The application uses a file named "tasks.txt" to store tasks and total task count.
- If "tasks.txt" doesn't exist, it will be created with an initial total task count of 0.
- The file structure is as follows:
  - Line 1: Application title
  - Line 2: Total task count
  - Lines 3 and onwards: List of tasks

## Future Iterations

- Make the application executable to easily share with others.
- Implement a graphical user interface (GUI) for a more user-friendly experience.
- Add the capability to convert the task list to PDF format.
- Include options to send the task list via email or SMS.

## Note

- This application requires Python 3.10 or later.
- Press Enter to continue after each operation.

## Author

Antoine Gaton

## Date

8/19/23