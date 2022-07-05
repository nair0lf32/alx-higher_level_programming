#!/usr/bin/python3
"""writes json to a file"""
import json


def save_to_json_file(my_obj, filename):
    """converts a string object to json and writes it to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
