#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a given letter
"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    q_data = {"q": q}
    response = requests.post(url, data=q_data)
    try:
        json_res = response.json()
        if json_res == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_res.get("id"), json_res.get("name")))
    except ValueError:
        print("Not a valid JSON")
