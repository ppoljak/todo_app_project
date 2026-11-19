# TO DO APP

Simple CLI-based To-Do App

## Features
- Create Task
- Read Tasks
- Update Task
- Delete Task

## Modules

`models.py` -- Task Object - e.g. Regular -- Recurring, Deadline are not implemented yet...
`controller.py` -- Manage the Task object -- Create, Read, Update, Delete ...   
`viewer_cli.py` -- CLI interaction with user -- Communication between user and controller    
`storage.py` -- Storage functions for storing and loading from .json files -- not implemented yet...   
`validation.py` -- Validation function for validating of user input
`main.py` -- Main file for running the app  

## How to Run

```bash
python -m main
```

## Next Improvements

- JSON persistance
- Recurring, Deadline Tasks ...
- Filtering, Sorting
- Statistics