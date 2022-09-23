#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
from requests import get


if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"

    response = get(url)
    b_content = response.text
    string = "Body response:\n\t- type: {}\n\t- content: {}"\
        .format(type(b_content), b_content)
