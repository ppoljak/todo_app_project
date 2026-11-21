from .models import Task, RecurringTask, DeadlineTask
from .storage import StorageFun as store

# Task Controller -- Managing Task Objects
class ToDoList:
    def __init__(self):
        self._tasks = store.load_from_json()

    def get_task(self, task_id: int = 0):
        """Retrieve tasks by their ID."""
        if task_id in range(0, len(self._tasks)):
            return self._tasks[task_id]

    def create_task(self, text: str, additional_info = None, task_type: str = "regular"):
        """Create a new task"""
        if task_type == "regular":
            self._tasks.append(Task(text))
        elif task_type == "recurring":
            self._tasks.append(RecurringTask(text, additional_info))
        elif task_type == "deadline":
            self._tasks.append(DeadlineTask(text, additional_info))
        store.save_to_json(self._tasks)

    def read_tasks(self):
        """Returns a list of tasks."""
        return self._tasks

    def update_task(self, task_id: int, text: str = None, toggle: bool = False, additional_info = None):
        """Selects a task by ID in the list of tasks and changes its attributes."""
        task = self.get_task(task_id)
        if not task:
            return
        if text:
            task.update_text(text)
        if toggle:
            task.toggle_done()
        if additional_info and isinstance(task, RecurringTask):
            task.update_frequency(additional_info)
        if additional_info and isinstance(task, DeadlineTask):
            task.update_deadline(additional_info)
        store.save_to_json(self._tasks)

    def delete_task(self, task_id: int):
        """Selects a task by ID in the list of tasks and deletes it."""
        if self.get_task(task_id):
            self._tasks.pop(task_id)
        store.save_to_json(self._tasks)