#!/usr/bin/python3
"""read add then save to json file"""
import json
import sys
import os.path
save_ = __import__('5-save_to_json_file').save_to_json_file
load_ = __import__('6-load_from_json_file').load_from_json_file


def read_add_save():
    """adds all arguments to a Python list,
        and then save them to a file"""

    filename = "add_item.json"
    args_list = []
    if os.path.exists(filename):
        args_list = load_(filename)

    args_list.extend(sys.argv[1:])
    save_(args_list, filename)


if __name__ == "__main__":
    read_add_save()
