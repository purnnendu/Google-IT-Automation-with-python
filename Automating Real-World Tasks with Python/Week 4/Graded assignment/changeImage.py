#!/usr/bin/env python3

import os
from PIL import Image

old_path = os.path.expanduser('~') + '/supplier-data/images/'
new_path = '/supplier-data/images/'

for image in os.listdir(old_path):
        if '.tiff' in image:
                img = Image.open(old_path + image)
                img.resize((600, 400)).convert("RGB").save(old_path + image.split('.')[0]+".jpeg", 'jpeg')
                img.close()
