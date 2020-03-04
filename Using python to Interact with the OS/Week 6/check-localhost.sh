#!/usr/bin/env bash

if grep "127.0.0.1" /etc/hosts; then
  echo "Everything is Ok!!"
else
  echo "ERROR! 127.0.0.1 is missing!"
fi

if test -n "$path"; then echo "Your path is not empty!"; fi
if [ -n "$path"]; then echo "Your path is not empty!"; fi
