# tasks.py

import tkinter as tk
import tkinter.messagebox as messagebox

def  display_tasks(tasks, task_frame, refreh_task, mark_task_done_func, delete_task_func):
    for widget in task_frame.winfo_children():
        widget.destroy()

    for index, task in enumerate(tasks):
        task_text = f"{task['title']} - {'Done' if task['done'] else 'Pending'}"

        task_label = tk.Label(task_frame, text=task_text, width=50, anchor="w")
        task_label.grid(row=index, column=0, sticky="w")

        if task["done"]:
            done_label = tk.Label(task_frame, text="Done", fg="green")
            done_label.grid(row=index, column=1, sticky="e")
        else:
            mark_done_button = tk.Button(task_frame, text="Mark as done", command=lambda i=index: mark_task_done_func(tasks, i, refreh_task))
            mark_done_button.grid(row=index, column=1, sticky="e")

        delete_button = tk.Button(task_frame, text="Delete", command=lambda i=index: delete_task_func(tasks, i, refreh_task))
        delete_button.grid(row=index, column=2, sticky="e")

def add_task(tasks, task_entry, refresh_tasks):
    #add new task to the list and refresh the gui
    task = task_entry.get()
    if task:
        tasks.append({"title": task, "done": False})
        task_entry.delete(0, "end")
        refresh_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task(tasks, index, refresh_tasks):
    del tasks[index]
    refresh_tasks()

def mark_task_done(tasks, index, refresh_tasks):
    tasks[index]["done"] = True
    refresh_tasks()