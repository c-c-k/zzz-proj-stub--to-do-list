import logging

from . import view, model

logger = logging.getLogger(__name__)


def controller(command):
    logger.debug(str(command))
    match command:
        # main menu
        case ["menu", "main"]:
            choice = view.get_menu_choice_main()
            next_command = ["menu_choice", "main", choice]
        case ["menu_choice", "main", "1"]:
            # 1. Print today's tasks
            next_command = ["menu", "tasks", "today"]
        case ["menu_choice", "main", "2"]:
            # 1. Print week's tasks
            next_command = ["menu", "tasks", "week"]
        case ["menu_choice", "main", "3"]:
            # 1. Print all tasks
            next_command = ["menu", "tasks", "all"]
        case ["menu_choice", "main", "4"]:
            # 2. Enter tasks_missed menu
            next_command = ["menu", "tasks", "missed"]
        case ["menu_choice", "main", "5"]:
            # 2. Enter task_add menu
            next_command = ["menu", "task_add"]
        case ["menu_choice", "main", "6"]:
            # 2. Enter task_delete menu
            next_command = ["menu", "task_delete"]
        case ["menu_choice", "main", "0"]:
            # 0. Exit
            next_command = ["exit"]

        # today's tasks menu
        case ["menu", "tasks", "today"]:
            tasks = model.tasks_get_today()
            next_command = ["menu", "tasks", "today", tasks]
        # Handle no tasks
        case ["menu", "tasks", "today", None]:
            view.print_no_tasks()
            next_command = ["menu", "main"]
        case ["menu", "tasks", "today", tasks]:
            view.print_tasks_today(tasks)
            next_command = ["menu", "main"]

        # week's tasks menu
        case ["menu", "tasks", "week"]:
            weekdays = model.Weekdays()
            next_command = ["menu", "tasks", "week", weekdays]
        case ["menu", "tasks", "week", weekdays]:
            weekday_info = weekdays.next()
            next_command = ["menu", "tasks", "week", weekdays, weekday_info]
        case ["menu", "tasks", "week", _, None]:
            # Handle finished weekdays
            view.print_separator_line()
            next_command = ["menu", "main"]
        case ["menu", "tasks", "week", weekdays, weekday_info]:
            view.print_separator_line()
            view.print_tasks_weekday(weekday_info)
            next_command = [
                "menu", "tasks", "week", weekdays]

        # all tasks menu
        case ["menu", "tasks", "all"]:
            tasks = model.tasks_get_all()
            next_command = ["menu", "tasks", "all", tasks]
        # Handle no tasks
        case ["menu", "tasks", "all", None]:
            view.print_no_tasks()
            next_command = ["menu", "main"]
        case ["menu", "tasks", "all", tasks]:
            view.print_separator_line()
            view.print_tasks_all(tasks)
            view.print_separator_line()
            next_command = ["menu", "main"]

        # missed tasks menu
        case ["menu", "tasks", "missed"]:
            tasks = model.tasks_get_missed()
            next_command = ["menu", "tasks", "missed", tasks]
        # Handle no tasks
        case ["menu", "tasks", "missed", None]:
            view.print_all_tasks_done()
            next_command = ["menu", "main"]
        case ["menu", "tasks", "missed", tasks]:
            view.print_separator_line()
            view.print_tasks_missed(tasks)
            view.print_separator_line()
            next_command = ["menu", "main"]

        # task_add menu
        case ["menu", "task_add"]:
            view.task_add()
            next_command = ["menu", "main"]

        # task_delete menu
        case ["menu", "task_delete"]:
            tasks = model.tasks_get_all()
            next_command = ["menu", "task_delete", tasks]
        # Handle no tasks
        case ["menu", "task_delete", None]:
            view.print_no_tasks()
            next_command = ["menu", "main"]
        case ["menu", "task_delete", tasks]:
            view.print_separator_line()
            view.task_delete(tasks)
            view.print_separator_line()
            next_command = ["menu", "main"]

        # exit program
        case ["exit"]:
            view.print_exit_message()
            exit()

        # catch all for unhandled commands
        case [*unhandled_command]:
            view.print_unhandled_command_message(unhandled_command)
            next_command = ["menu", "main"]

    return next_command
