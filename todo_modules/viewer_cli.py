from .validation import ValidationFun as valid

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
        text = valid.is_empty("Enter a new task")
        self._controller.create_task(text)

    def read_tasks_cli(self):
        if not self._tasks:
            print("No tasks to show.")
            return
        print_enumerated(self._tasks)

    def update_task_cli(self):
        if not self._tasks:
            print("No task to update.")
            return
        
        options = ["update text", "toggle status"]
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