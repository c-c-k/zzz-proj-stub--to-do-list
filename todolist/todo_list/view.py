import itertools

from . import messages as msg
from . import model


def print_message(message):
    print(message.strip())


def get_user_input(message):
    print_message(message)
    return input().strip()


# main menu
def get_menu_choice_main():
    return get_user_input(msg.MENU_MAIN)


# task_add menu
def task_add():
    task_data = {'task': get_user_input(msg.PROMPT_NEW_TASK)}
    model.task_create(task_data)
    print_message(msg.INFO_TASK_ADDED)


# tasks_today menu
def print_no_tasks():
    print_message(msg.ERROR_NO_TASKS)


def print_tasks_today(tasks):
    print_message(msg.INFO_TODAY)
    for menu_index, task in zip(itertools.count(1), tasks):
        print_message(
            msg.INFO_TASK_ENTRY.substitute(
                menu_index=menu_index, task=task.task
            ))


# exit
def print_exit_message():
    print_message(msg.INFO_GOODBYE)


# unhandled command
def print_unhandled_command_message(*unhandled_command):
    print("ERROR: unhandled_command: ", unhandled_command)
