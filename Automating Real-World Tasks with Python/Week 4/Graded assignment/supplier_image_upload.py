#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
path = os.path.expanduser('~') + '/supplier-data/images/'
images = [i for i in sorted(os.listdir(path)) if ".jpeg" in i]


for image in images:
        with open(path + image, 'rb') as opened:
                r = requests.post(url, files={'file': opened})
