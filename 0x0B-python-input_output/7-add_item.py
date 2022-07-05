#!/usr/bin/python3
"""read add then save to json file"""
import json
import sys
save_ = __import__('5-save_to_json_file').save_to_json_file
load_ = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    """adds all arguments to a Python list,
    and then save them to a file"""
    try:
        args = load_("add_item.json")
    except FileNotFoundError:
        args = []
    args.extend(sys.argv[1:])
    save_(args, "add_item.json")
