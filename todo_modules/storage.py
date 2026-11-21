import json
from .models import Task, RecurringTask, DeadlineTask
import datetime as dt

# Storage Object -- contains function for storing and loading data from .json files
class StorageFun:
    @staticmethod
    def load_from_json(file_name: str = "tasks.json"):
        """Loads the task list from .json file."""
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
                elif task["task_type"] == "recurring":
                    tasks.append(RecurringTask(task["text"], task["frequency"], task["done"]))
                elif task["task_type"] == "deadline":
                    try:
                        deadline = dt.datetime.strptime(task["deadline"], "%d.%m.%Y.").date()
                    except ValueError:
                        deadline = dt.date.today()
                    tasks.append(DeadlineTask(task["text"], deadline, task["done"]))
            except KeyError:
                continue
        return tasks

    @staticmethod 
    def save_to_json(data: list, file_name: str = "tasks.json"):
        """Save the task list to the .json file."""
        tasks = {}
        for task_id, task in enumerate(data, 1):
            tasks[task_id] = task.to_dict()

        with open(file_name, "w", encoding= "utf-8") as f:
            json.dump(tasks, f, indent = 4, ensure_ascii = False)