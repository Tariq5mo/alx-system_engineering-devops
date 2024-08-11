# 0x15. API

## Overview

The **0x15. API** project focuses on building Python scripts to interact with APIs and organize employee data. As system administrators transition from Bash scripting to more efficient programming languages, understanding APIs becomes crucial. In this project, we explore the following concepts:

1. **What Bash Scripting Should Not Be Used For**: While Bash is useful, it can get messy and inefficient for certain tasks.
2. **What Is an API**: An Application Programming Interface (API) allows interaction with an application or service.
3. **What Is a REST API**: A type of API that follows REST principles for communication.
4. **Microservices**: APIs often serve as the public-facing part of microservices.
5. **Data Formats**: Understanding CSV and JSON formats.
6. **Pythonic Naming Conventions**: Proper naming styles for packages, classes, variables, functions, and constants.

## Project Tasks

1. **Gather Data from an API**: Write a Python script that retrieves TODO list progress for a given employee ID using a REST API.
2. **Export to CSV**: Extend the script to export data in CSV format, recording tasks owned by each employee.
   - Format: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`
   - File name: `USER_ID.csv`
3. **Export to JSON**: Further extend the script to export data in JSON format.
   - Format: `{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}`
   - File name: `USER_ID.json`
4. **Dictionary of List of Dictionaries**: Export all tasks from all employees in JSON format.
   - Format: `{ "USER_ID": [{"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}`
   - File name: `todo_all_employees.json`
