#!/usr/bin/python3
"""Using what you did in the task #0,
extend previous Python script to export data in the CSV format.
"""
import csv
import json
from requests import get, request
from sys import argv


if __name__ == "__main__":
    if (argv[1]).isdigit():
        id_employee = argv[1]
        """ fetch the name of employee. """
        resp_name = get("https://jsonplaceholder.typicode.com/users?id={}".
                        format(id_employee))
        list_dict = resp_name.json()
        for n in list_dict:
            if n.get("username", None) is not None:
                username = n.get("username")
                break
        resp_todo = get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(id_employee))
        mydict = resp_todo.json()

        fields = ['userId', "USERNAME", 'completed', "title"]

        with open('{}.csv'.format(id_employee), 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fields,
                                    restval=username, extrasaction="ignore",
                                    quoting=csv.QUOTE_ALL)

            writer.writerows(mydict)
