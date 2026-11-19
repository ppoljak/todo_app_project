import json
from .models import Task

# Storage Object -- contains function for storing and loading data from .json files
class StorageFun:
    @staticmethod
    def load_from_json(file_name: str = "tasks.json"):
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                task_dict = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("The file does not exist or is damaged.")
            return []
        
        tasks = [] 
          
        for i, task in task_dict.items():
            try:
                if task["task_type"] == "regular":
                    tasks.append(Task(task["text"], task["done"]))
            except KeyError:
                continue
        return tasks

    @staticmethod 
    def save_to_json(data: list, file_name: str = "tasks.json"):
        tasks = {}
        for task_id, task in enumerate(data, 1):
            tasks[task_id] = task.to_dict()
        with open(file_name, "w", encoding= "utf-8") as f:
            json.dump(tasks, f, indent = 4, ensure_ascii = True)