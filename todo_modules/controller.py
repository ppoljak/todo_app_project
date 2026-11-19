from .models import Task

# Task Controller -- Managing Task Objects
class ToDoList:
    def __init__(self):
        self._tasks = []

    def get_task(self, task_id: int = 0):
        """Retrieve tasks by their ID."""
        if task_id in range(0, len(self._tasks)):
            return self._tasks[task_id]

    def create_task(self, text: str, additional_info = None, task_type: str = "regular"):
        """Create a new task"""
        if task_type == "regular":
            self._tasks.append(Task(text))

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

    def delete_task(self, task_id: int):
        """Selects a task by ID in the list of tasks and deletes it."""
        if self.get_task(task_id):
            self._tasks.pop(task_id)