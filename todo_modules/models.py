import datetime as dt

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
        """Export task to dictionary"""
        return {
            "task_type": "regular", 
            "text": self._text, 
            "done": self._done
        }

# Recurring Task
class RecurringTask(Task):
    def __init__(self, text: str, frequency: str, done: bool = False):
        super().__init__(text, done)
        self._frequency = frequency
    
    def __str__(self):
        return f"{super().__str__()} | {self._frequency}"

    def update_frequency(self, frequency: str):
        """Change the task frequency."""
        self._frequency = frequency

    def to_dict(self):
        """Export task to dictionary."""
        return {
            "task_type": "recurring", 
            "text": self._text, 
            "done": self._done, 
            "frequency": self._frequency
        }

# Deadline Task
class DeadlineTask(Task):
    def __init__(self, text: str, deadline: dt.date, done: bool = False):
        super().__init__(text, done)
        self._deadline = deadline
    
    def __str__(self):
        return f"{super().__str__()} | {self._deadline:%d.%m.%Y.} | {self.importance}"

    def update_deadline(self, deadline: dt.date):
        """Change the task deadline."""
        self._deadline = deadline

    def days_left(self):
        """Counts days till deadline."""
        remain_days = self._deadline - dt.date.today()
        return remain_days.days
    
    @property
    def importance(self):
        #Calculate the importance based on days left
        if self.days_left() <= 3:
            return "HIGH"
        elif self.days_left() <= 7:
            return "MEDIUM"
        else:
            return "LOW"

    def to_dict(self):
        """Export task to dictionary."""
        return {
            "task_type": "deadline", 
            "text": self._text, 
            "done": self._done, 
            "deadline": f"{self._deadline:%d.%m.%Y.}"
        }