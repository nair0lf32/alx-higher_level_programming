#!/usr/bin/python3
"""read json from a file"""
import json


def load_from_json_file(filename):
    """creates a string object from a json file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
