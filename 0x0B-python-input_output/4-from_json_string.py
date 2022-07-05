#!/usr/bin/python3
"""json to string converter"""
import json


def from_json_string(my_str):
    """convert a json to a python string object"""
    return json.loads(my_str)
