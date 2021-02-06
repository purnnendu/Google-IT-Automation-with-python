#! /usr/bin/env python3

import os
import requests
import json

path = os.path.expanduser('~') + '/supplier-data/descriptions/'
files = sorted(os.listdir(path))
url = 'http://35.225.80.24/fruits/'
fruit = {}

for file in files:
    fruit.clear()
    with open(path + file) as f:
        line = f.readlines()
        fruit["name"] = line[0].strip('\n')
        fruit["weight"] = int(line[1].strip('\n').strip('lbs'))
        fruit["description"] = line[2].strip('\n')
        fruit["image_name"] = (file.strip('.txt'))+'.jpeg'
        print(fruit)
        #print(json.dumps(fruit, indent = 2))
        print()
"""     response=requests.post("http://35.225.80.24/fruits/",json = fruit)
        print(response.request.url)
        print(response.status_code)
"""
