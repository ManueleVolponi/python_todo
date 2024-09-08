# main.py

import tkinter as tk
from tkinter import simpledialog 
from tasks import add_task, display_tasks, mark_task_done, delete_task
from file_io import load_tasks, save_tasks

def main():
    # Initialize the Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the main window initially

    # Prompt for the to-do list file name using a dialog box
    todolist_name = simpledialog.askstring("To-Do List", "Enter the name of the to-do list file:")
    
    if not todolist_name:
        # If the user cancels or enters nothing, exit the app
        print("No file name provided. Exiting.")
        root.quit()
        return

    # Set the file path dynamically based on the user input
    file = f"{todolist_name}.json"
    
    # Load tasks from the specified file
    tasks = load_tasks(file)

    # Show the main window after file name is entered
    root.deiconify()
    root.title(f"{todolist_name} - To Do List")

    # entry field to add new tasks
    task_entry = tk.Entry(root, width=50)
    task_entry.pack(pady=10)

    # entry frame to display tasks
    task_frame = tk.Frame(root)
    task_frame.pack(pady=10)

    # Refresh task display
    def refresh_tasks():
        display_tasks(tasks, task_frame, refresh_tasks, mark_task_done, delete_task)

    # Add task button
    add_task_button = tk.Button(root, text="Add Task", command=lambda: add_task(tasks, task_entry, refresh_tasks))
    add_task_button.pack(pady=10, padx=5)

    # Display the initial list of tasks
    refresh_tasks()

    def on_closing():
        save_tasks(file, tasks)
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    #start Thinker event loop
    root.mainloop()

if __name__ == "__main__":
    main()