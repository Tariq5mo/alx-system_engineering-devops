#!/usr/bin/python3
"""Using what you did in the task #0,
extend previous Python script to export data in the CSV format.
"""
import json
from requests import get


if __name__ == "__main__":
    """ fetch the name of employees and their ID's. """
    resp_name = get("https://jsonplaceholder.typicode.com/users/")
    list_dict = resp_name.json()
    dict_employees = {}
    for n in list_dict:
        if n.get("username", None) is not None:
            inner_dict = {}
            inner_dict["username"] = n.get("username")
            inner_dict["id"] = n.get("id")
            dict_employees[n.get("id")] = inner_dict
    mydict = {}
    for id_employee in dict_employees:
        resp_todo = get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(id_employee))
        mylist = resp_todo.json()
        for di in mylist:
            di["username"] = dict_employees[id_employee]["username"]
            value = dict(di).get("title")
            di.pop("title")
            di["task"] = value
            di.pop("userId")
            di.pop("id")
            value = dict(di).get("completed")
            di.pop("completed")
            di["completed"] = value
        mydict[id_employee] = mylist

    with open('todo_all_employees.json', 'w') as file:
        json.dump(mydict, file)
