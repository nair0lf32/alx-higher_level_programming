
#!/usr/bin/python3
"""
Uses the GitHub API to display a GitHub id based on given credentials
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    usrname = sys.argv[1]
    passwd = sys.argv[2]
    auth = HTTPBasicAuth(usrname, passwd)
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
