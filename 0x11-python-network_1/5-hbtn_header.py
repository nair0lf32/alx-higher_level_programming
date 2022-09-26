#!/usr/bin/python3
"""
Sends a request to given URL and displays the X-Request-Id response header
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
