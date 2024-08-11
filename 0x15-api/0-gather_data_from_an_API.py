#!/usr/bin/python3
from sys import argv
from requests import get, request
import json


if __name__ == "__main__":
    if (argv[1]).isdigit():
        id_employee = argv[1]
        """ fetch the name of employee. """
        resp_name = get("https://jsonplaceholder.typicode.com/users?id={}".
                        format(id_employee))
        list_dict = resp_name.json()
        for n in list_dict:
            if n.get("name", None) is not None:
                name = n.get("name")
                break
        resp_todo = get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(id_employee))
        todo_list = resp_todo.json()
        all_todo = len(todo_list)
        completed_todo = []
        for di in todo_list:
            if di.get("completed", None) is True:
                completed_todo.append(di.get("title"))
        print("Employee {} is done with tasks({}/{}):".
              format(name, len(completed_todo), all_todo))
        for do in completed_todo:
            print('\t' + ' ' + do)
