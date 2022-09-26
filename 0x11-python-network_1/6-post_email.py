#!/usr/bin/python3
"""
Sends a POST request to given URL with the given email
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
