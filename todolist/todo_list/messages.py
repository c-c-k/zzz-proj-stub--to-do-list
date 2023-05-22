from string import Template


ERROR_NO_TASKS = "Nothing to do!"
INFO_GOODBYE = "Bye!"
INFO_TASKS_ALL_DONE = "All tasks have been completed!"
INFO_TASKS_TODAY = Template("Today ${date}:")  # date format '%d %b'
INFO_TASKS_WEEK_DAY = Template("${date}:")  # date format '%A %d %b'
INFO_TASKS_ALL = "All tasks:"
INFO_TASKS_MISSED = "Missed tasks:"
INFO_TASK_ENTRY = Template("${menu_index} ${task}")
INFO_TASK_ENTRY_WITH_DATE = Template(
        "${menu_index} ${task}. ${date}")  # date format '%d %b'
INFO_TASK_ENTRY_WITH_DATE_NO_INDEX = Template(
        "${task}. ${date}")  # date format '%d %b'
INFO_TASK_ADDED = "The task has been added!"
INFO_TASK_DELETED = "The task has been deleted!"
MENU_MAIN = """
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add a task
6) Delete a task
0) Exit
""".lower()
PROMPT_NEW_TASK = "Enter a task"
PROMPT_NEW_TASK_DEADLINE = "Enter a Deadline"
PROMPT_DELETE_TASK = "Choose the number of the task you want to delete:"
