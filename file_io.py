# file_io.py
import json

def load_tasks(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(file, tasks):
    with open(file, "w") as f:
        json.dump(tasks, f)