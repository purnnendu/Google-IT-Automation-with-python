#!/usr/bin/env bash

for file in *.HTM; do
  #statements remove echo to raname the file with .html extension
  name=$(basename $file .HTM)
  echo mv "$file" "$name.html
done
