from .validation import ValidationFun as valid
from .models import RecurringTask, DeadlineTask

#utility functions
def print_enumerated(items: list):
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")

# Task Viewer -- Interaction between User and Controller
class ViewerCLI:
    def __init__(self, controller):
        self._controller = controller
        self._tasks = controller.read_tasks()
        self._commands = [
            "create task",
            "read tasks",
            "update task",
            "delete task",
            "exit"
        ]

    def run_app(self):
        while True:
            print(f"{'='*50}\n")
            command = self.select_command()
            print()
            if command == "exit":
                print("Exiting the programm...")
                print(f"\n{'='*50}\n")
                return
            self.match_command(command)
            print()

    def select_command(self):
        print_enumerated(self._commands)
        print()
        command_id = valid.valid_number("Choose an actions", self._commands)
        return self._commands[command_id]

    def match_command(self, command):
        if command == "create task":
            self.create_task_cli()
        elif command == "read tasks":
            self.read_tasks_cli()
        elif command == "update task":
            self.update_task_cli()
        elif command == "delete task":
            self.delete_task_cli()

    def create_task_cli(self):
        task_types = ["regular", "recurring", "deadline"]
        option = valid.valid_option("Select the task type", task_types)
        print()
        text = valid.is_empty("Enter a new task")
        print()
        if option == "regular":
            self._controller.create_task(text)
        elif option == "recurring":
            frequencies = ["daily", "weekly", "monthly", "yearly"]
            frequency = valid.valid_option("Select the frequency", frequencies).upper()
            self._controller.create_task(text, frequency, option)
        elif option == "deadline":
            deadline = valid.validate_date("Enter the deadline")
            self._controller.create_task(text, deadline, option)
                    
    def read_tasks_cli(self):
        if not self._tasks:
            print("No tasks to show.")
            return
        print_enumerated(self._tasks)

    def update_task_cli(self):
        if not self._tasks:
            print("No task to update.")
            return
        
        options = ["update text", "toggle status", "update frequency", "update deadline"]
        print_enumerated(options)
        print()
        option_id = valid.valid_number("Choose an option", options)
        print()

        self.read_tasks_cli()
        print()
        task_id = valid.valid_number("Select the task", self._tasks)
        print()

        if options[option_id] == "update text":
            new_text = valid.is_empty("Edit task text")
            print()
            if valid.ask_yes_no("Are you sure you want to change the text of the task?"):
                self._controller.update_task(task_id, new_text)

        if options[option_id] == "toggle status":
            self._controller.update_task(task_id, toggle = True)

        if options[option_id] == "update frequency":
            if isinstance(self._tasks[task_id], RecurringTask):
                frequencies = ["daily", "weekly", "monthly", "yearly"]
                new_frequency = valid.valid_option("Select the new frequency", frequencies).upper()
                self._controller.update_task(task_id, additional_info = new_frequency)
            else:
                print("Selected task is not recurring.")

        if options[option_id] == "update deadline":
            if isinstance(self._tasks[task_id], DeadlineTask):
                new_deadline = valid.validate_date("Enter the new deadline")
                self._controller.update_task(task_id, additional_info = new_deadline)
            else:
                print("Selected task is not deadline.")
        

    def delete_task_cli(self):
        if not self._tasks:
            print("No task to delete.")
            return
        
        self.read_tasks_cli()
        print()
        task_id = valid.valid_number("Select the task", self._tasks)
        print()
        if valid.ask_yes_no("Are you sure you want to delete the task?"):
            self._controller.delete_task(task_id)