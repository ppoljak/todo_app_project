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

    def search_tasks(self, user_input: str):
        """Returns a list of tasks based on the user's search."""
        searched_tasks = list(filter(lambda task: user_input.lower() in task._text.lower(), self._tasks))
        return searched_tasks

    def filter_tasks(self):
        """Returns a dictionary with data filtered by completion status and task type."""
        completed = list(filter(lambda task: task._done, self._tasks))
        pending = list(filter(lambda task: not task._done, self._tasks))
        regular = list(filter(lambda task: type(task) == Task, self._tasks))
        recurring = list(filter(lambda task: isinstance(task, RecurringTask), self._tasks))
        deadline = list(filter(lambda task: isinstance(task, DeadlineTask), self._tasks))
        return {
            "completed": completed,
            "pending": pending,
            "regular": regular,
            "recurring": recurring,
            "deadline": deadline
        }

    @staticmethod
    def sort_fun(task):
        if isinstance(task, DeadlineTask):
            return (1, task.days_left())
        elif isinstance(task, RecurringTask):
            order = {"DAILY": 0, "WEEKLY": 1, "MONTHLY": 2, "YEARLY": 3}
            return (2, order.get(task._frequency, 99))
        else:
            return (3, 0)

    def sort_by_importance(self):
        """Returns sorted list of task based on the importance."""
        return sorted(self._tasks, key = self.sort_fun)

    def statistics(self):
        """Returns statistics on the completion of tasks."""
        total = len(self._tasks)
        completed = len(list(filter(lambda task: task._done, self._tasks)))
        pending = len(list(filter(lambda task: not task._done, self._tasks)))
        percentage = round(completed/total*100, 0) if total else 0
        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "percentage": percentage
        }