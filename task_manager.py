#!/usr/bin/env python3
import argparse
import os
import sys

# ANSI color codes for basic colors
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

tasks = []

def add_task(task):
    tasks.append({'task': task, 'completed': False})

def list_tasks():
    if not tasks:
        print(f"{colors.WARNING}No tasks found.{colors.ENDC}")
    else:
        for i, task in enumerate(tasks, start=1):
            status = '[x]' if task['completed'] else '[ ]'
            color = colors.OKGREEN if task['completed'] else colors.OKBLUE
            print(f"{color}{i}. {status} {task['task']}{colors.ENDC}")

def complete_task(task_num):
    if task_num <= 0 or task_num > len(tasks):
        print(f"{colors.WARNING}Invalid task number.{colors.ENDC}")
    else:
        tasks[task_num - 1]['completed'] = True

def uncomplete_task(task_num):
    if task_num <= 0 or task_num > len(tasks):
        print(f"{colors.WARNING}Invalid task number.{colors.ENDC}")
    else:
        tasks[task_num - 1]['completed'] = False

def complete_all_tasks():
    for task in tasks:
        task['completed'] = True

def uncomplete_all_tasks():
    for task in tasks:
        task['completed'] = False

def clear_completed_tasks():
    global tasks
    tasks = [task for task in tasks if not task['completed']]
    print(f"{colors.OKGREEN}Completed tasks cleared.{colors.ENDC}")

def clear_all_tasks():
    global tasks
    tasks = []
    print(f"{colors.OKGREEN}All tasks cleared.{colors.ENDC}")

def save_tasks(filename):
    try:
        with open(filename, 'w') as f:
            for task in tasks:
                f.write(f"{task['task']}|{task['completed']}\n")
        print(f"{colors.OKGREEN}Tasks saved to '{filename}'.{colors.ENDC}")
    except IOError:
        print(f"{colors.WARNING}Error saving tasks to '{filename}'.{colors.ENDC}")

def load_tasks(filename):
    global tasks
    tasks = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                task_info = line.strip().split('|')
                task = {'task': task_info[0], 'completed': task_info[1] == 'True'}
                tasks.append(task)
        print(f"{colors.OKGREEN}Tasks loaded from '{filename}'.{colors.ENDC}")
    except FileNotFoundError:
        print(f"{colors.WARNING}File '{filename}' not found. Starting with an empty task list.{colors.ENDC}")
    except IOError:
        print(f"{colors.WARNING}Error loading tasks from '{filename}'. Starting with an empty task list.{colors.ENDC}")

def main():
    parser = argparse.ArgumentParser(description="Command-line task manager")
    parser.add_argument('command', choices=['add', 'list', 'complete', 'uncomplete', 'complete-all', 'uncomplete-all', 'clear-completed', 'clear-all'],
                        help="Command to execute")
    parser.add_argument('--task', '-a', help="Task description")
    parser.add_argument('--task-num', '-n', type=int, help="Task number")
    parser.add_argument('--file', '-f', help="File to save/load tasks (must end with .txt or .md)")

    args = parser.parse_args()

    if args.file:
        if not args.file.lower().endswith(('.txt', '.md')):
            print(f"{colors.WARNING}File must end with .txt or .md extension.{colors.ENDC}")
            sys.exit(1)
        filename = args.file
    else:
        filename = "tasks.txt"

    load_tasks(filename)

    if args.command == 'add':
        if args.task:
            add_task(args.task)
        else:
            print(f"{colors.WARNING}Please provide a task description using '--task' or '-a'.{colors.ENDC}")

    elif args.command == 'list':
        list_tasks()

    elif args.command == 'complete':
        if args.task_num:
            complete_task(args.task_num)
        else:
            print(f"{colors.WARNING}Please provide a task number to complete using '--task-num' or '-n'.{colors.ENDC}")

    elif args.command == 'uncomplete':
        if args.task_num:
            uncomplete_task(args.task_num)
        else:
            print(f"{colors.WARNING}Please provide a task number to mark as incomplete using '--task-num' or '-n'.{colors.ENDC}")

    elif args.command == 'complete-all':
        complete_all_tasks()

    elif args.command == 'uncomplete-all':
        uncomplete_all_tasks()

    elif args.command == 'clear-completed':
        clear_completed_tasks()

    elif args.command == 'clear-all':
        confirm = input("Are you sure you want to clear all tasks? (y/N): ").strip().lower()
        if confirm == 'y':
            clear_all_tasks()
        else:
            print("Operation canceled.")
            sys.exit()

    else:
        parser.print_help()

    save_tasks(filename)

if __name__ == "__main__":
    main()
