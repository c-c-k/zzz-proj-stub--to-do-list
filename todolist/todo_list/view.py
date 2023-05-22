from datetime import datetime
import itertools
import logging

from . import messages as msg
from . import model

logger = logging.getLogger(__name__)


def print_separator_line():
    print()


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
    task = get_user_input(msg.PROMPT_NEW_TASK)
    deadline = get_user_input(msg.PROMPT_NEW_TASK_DEADLINE)
    task_data = {
        'task': task,
        'deadline': datetime.strptime(deadline, "%Y-%m-%d")
    }
    model.task_create(task_data)
    print_message(msg.INFO_TASK_ADDED)


# tasks today/week/all menus
def print_no_tasks():
    print_message(msg.ERROR_NO_TASKS)


def print_tasks_today(tasks):
    print_message(
        msg.INFO_TASKS_TODAY.substitute(
            date=datetime.today().strftime('%d %b')))
    for menu_index, task in zip(itertools.count(1), tasks):
        print_message(
            msg.INFO_TASK_ENTRY.substitute(
                menu_index=menu_index, task=task.task))


def print_tasks_weekday(weekday_info):
    print_message(
        msg.INFO_TASKS_WEEK_DAY.substitute(
            date=weekday_info["date"].strftime('%A %d %b')))
    if weekday_info["tasks"] is None:
        print_message(msg.ERROR_NO_TASKS)
        return
    for menu_index, task in zip(itertools.count(1), weekday_info["tasks"]):
        print_message(
            msg.INFO_TASK_ENTRY.substitute(
                menu_index=menu_index, task=task.task))


def print_tasks_all(tasks):
    print_message(msg.INFO_TASKS_ALL)
    for task in tasks:
        print_message(
            msg.INFO_TASK_ENTRY_WITH_DATE.substitute(
                task=task.task,
                date=task.deadline.strftime('%d %b')))


# exit
def print_exit_message():
    print_message(msg.INFO_GOODBYE)


# unhandled command
def print_unhandled_command_message(*unhandled_command):
    print("ERROR: unhandled_command: ", unhandled_command)
