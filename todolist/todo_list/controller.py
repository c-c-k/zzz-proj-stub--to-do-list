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
            next_command = ["menu", "tasks_today"]
        case ["menu_choice", "main", "2"]:
            # 2. Enter task_add menu
            next_command = ["menu", "task_add"]
        case ["menu_choice", "main", "0"]:
            # 0. Exit
            next_command = ["exit"]

        # task_add menu
        case ["menu", "task_add"]:
            view.task_add()
            next_command = ["menu", "main"]

        # today's tasks menu
        case ["menu", "tasks_today"]:
            tasks = model.tasks_get_all()
            next_command = ["menu", "tasks_today", tasks]
        case ["menu", "tasks_today", None]:
            # Handle no tasks
            view.print_no_tasks()
            next_command = ["menu", "main"]
        case ["menu", "tasks_today", tasks]:
            view.print_tasks_today(tasks)
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
