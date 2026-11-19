# Task Objects

# Regular Task
class Task:
    def __init__(self, text: str, done: bool = False):
        self._text = text
        self._done = done

    def __str__(self):
        return f"{"☑" if self._done else "☒"} {self._text}"

    def toggle_done(self):
        """Change the task status."""
        self._done = not self._done

    def update_text(self, text: str):
        """Change the task text."""
        self._text = text

    def to_dict(self):
        """Saving the task in the dictionary when exporting to json"""
        return {"task_type": "regular", "text": self._text, "done": self._done}

# Recurring Task
class RecurringTask(Task):
    def __init__(self, text: str, frequency: str, done: bool = False):
        super().__init__(text, done)
        self._frequency = frequency
    
    def __str__(self):
        return f"{super().__str__()} | {self._frequency}"

# Deadline Task
class DeadlineTask(Task):
    def __init__(self, text: str, deadline, done: bool = False):
        super().__init__(text, done)
        self._deadline = deadline
    
    def __str__(self):
        return f"{super().__str__()} | {self._deadline}"