from string import Template


ERROR_NO_TASKS = "Nothing to do!"
INFO_GOODBYE = "Bye!"
INFO_TASKS_TODAY = Template("Today ${date}:")  # date format '%d %b'
INFO_TASKS_WEEK_DAY = Template("${date}:")  # date format '%A %d %b'
INFO_TASKS_ALL = "All tasks:"
INFO_TASK_ENTRY = Template("${menu_index} ${task}")
INFO_TASK_ENTRY_WITH_DATE = Template(
        "${task}. ${date}")  # date format '%d %b'
INFO_TASK_ADDED = "The task has been added!"
MENU_MAIN = """
1) Today's tasks
2) Week's tasks
3) All tasks
4) Add a task
0) Exit
""".lower()
PROMPT_NEW_TASK = "Enter a task"
PROMPT_NEW_TASK_DEADLINE = "Enter a Deadline"
