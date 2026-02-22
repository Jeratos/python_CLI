# Python CLI Task Manager

A simple, interactive command-line interface (CLI) application for managing a temporary task list, built in Python.

## Structure

- `cli-env/module.py`: The main script containing the interactive task loop.

## Usage

To start the task manager, navigate to the `cli-env` directory or run the `module.py` script with the `task` argument:

```bash
python cli-env/module.py task
```

Once the interactive prompt starts (`>>`), you can use the following commands:

- `add`: Prompts you to enter a new task to add to the list.
- `show`: Displays the count and details of all your current tasks.
- `q`: Exits the task manager terminal.

## Example

```text
> python cli-env/module.py task
now enter your commant
>> add
enter your task here :Buy groceries
your task is been added to the list
 and your task is: Buy groceries
>> show
your task length is 1
your task is:
 Buy groceries
>> q
exit to the task terminal...
```
