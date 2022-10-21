#!/usr/bin/python3
"""
Send a post request to a specific url and display the results depending
on the passed in parameter and if the response is JSON formatted
"""
import requests
import sys


def search_api():
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    new_dict = {'q': q}
    req = requests.post("http://0.0.0.0:5000/search_user", new_dict)

    try:
        user = req.json()
        if user:
            print("[{}] {}".format(user.get('id'), user.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")


if __name__ == '__main__':
    search_api()
