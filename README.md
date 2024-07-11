# Command-line Task Manager

A Simple (suck-less) and hackable command-line tool for managing tasks with Python.

# Installation

- Clone the repository:

   ```bash
   git clone https://github.com/atrebyy/task-manager.git
   cd task-manager
   sudo cp task_manager.py /usr/local/bin
   cd /urs/local/bin
   sudo mv task_manager.py <command-name> # example: tm

# Usage

- Add a task
   ```bash
   tm add -t "Task description"

- List tasks
   ```bash
   tm list

- Complete a task
   ```bash
   tm complete -n 1

- Clear completed tasks
   ```bash
   tm clear

- Clear all tasks
   ```bash
   tm clear -n all

- Save tasks
  ```bash
   tm save

- Load tasks
  ```bash
  tm load

# Contributing
Contributions are welcome if they are more suck-less ofc ;)! Please fork the repository and submit a pull request.

# License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/atrebyy/task-manager/blob/main/LICENSE) file for details.
