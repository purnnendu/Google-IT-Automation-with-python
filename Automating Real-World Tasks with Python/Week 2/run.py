#!/usr/bin/env python3

import os
import requests

files = os.listdir("/data/feedback")
d = {}
keys = ["title", "name", "date", "feedback"]

for f in files:
        with open("/data/feedback/"+f) as file:
                content = file.readlines()
                for i in range(4):
                        d[keys[i]] = content[i].rstrip()
        response = requests.post("http://35.184.30.95/feedback/", data = d)
        if response.status_code == 201:
                print("Success")
        elif not response.ok:
                raise Exception("POST failed with status code  {}".format(response
.status_code))
