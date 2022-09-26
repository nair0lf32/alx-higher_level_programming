#!/usr/bin/python3
"""
Sends a request to given URL and displays the body of the response
"""
import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            print(response.read().decode("utf8"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
