#!/usr/bin/python3
"""
Get the X-Request-ID of the passed in website argument.
Requests version
"""
import requests
import sys


def response_header():
    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-ID'))

if __name__ == '__main__':
    response_header()
