from string import Template


ERROR_NO_TASKS = "Nothing to do!"
INFO_GOODBYE = "Bye!"
INFO_TODAY = "Today:"
INFO_TASK_ADDED = "The task has been added!"
INFO_TASK_ENTRY = Template("${menu_index} ${task}")
MENU_MAIN = """
1) Today's tasks
2) Add a task
0) Exit
"""
PROMPT_NEW_TASK = "Enter a task"
