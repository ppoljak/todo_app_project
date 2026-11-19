from todo_modules.viewer_cli import ViewerCLI
from todo_modules.controller import ToDoList

if __name__ == "__main__":
    control = ToDoList()
    view = ViewerCLI(control)
    view.run_app()