# main.py

import tkinter as tk
# from tkinter import ttk
from tkinter import simpledialog, filedialog
from tasks import add_task, display_tasks, mark_task_done, delete_task
from file_io import load_tasks, save_tasks
import os
import json

def init():
    # Initialize the Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the main window initially

    # Set the initial directory path
    initial_dir = os.path.join(os.getcwd(), 'task_files')

    # Ensure the directory exists
    if not os.path.exists(initial_dir):
        os.makedirs(initial_dir)

    # TODO: Implement a combobox to select or create a new file
    # try to use combobox instead of file loader
    # list_files = [f for f in os.listdir(initial_dir) if f.endswith('.json')]
    # list_files.append("Create a new file")
    
    # combobox = ttk.Combobox(root, values=list_files)
    # combobox.pack(pady=10)

    # combobox.set("Select a file or create a new one")


    # if combobox.get() == "Create a new file":
    #     todolist_name = simpledialog.askstring("To-Do List", "Enter the name of the new to-do list file:")
    #     if todolist_name:
    #         if not todolist_name.endswith('.json'):
    #             todolist_name += '.json'
    #         if not os.path.exists(todolist_name):
    #             with open(todolist_name, 'w') as file:
    #                 json.dump([], file)
    #     else:
    #         root.destroy()
    #         return
    # else:
    #     todolist_name = combobox.get()

    # Ask the user to select or create a file
    todolist_name = filedialog.askopenfilename(
        defaultextension=".json",
        title="Select a To-Do List File",
        filetypes=(("JSON files", "*.json"),),
        initialdir = initial_dir
    )
    
    # If no file is selected, prompt to create a new one
    if not todolist_name:
        todolist_name = simpledialog.askstring("To-Do List", "Enter the name of the new to-do list file:")
        if todolist_name:
            if not todolist_name.endswith('.json'):
                todolist_name += '.json'
            if not os.path.exists(todolist_name):
                path = os.path.join(initial_dir, todolist_name)
                with open(path, 'w') as file:
                    json.dump([], file)
        else:
            root.destroy()
            return
        
    return root, todolist_name, initial_dir

def main():
    root, todolist_name, initial_dir = init()
        
    if not todolist_name:
        # If the user cancels or enters nothing, exit the app
        print("No file name provided. Exiting.")
        root.quit()
        return

    # Set the file path dynamically based on the user input
    file = os.path.join(initial_dir, todolist_name)
    
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
    task_frame.pack(pady=10, padx=20)

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