#!/usr/bin/env bash

n=1
while [[ $n -le 5 ]]; do
  #statements
  echo "Iteration number $n"
  ((n+=1))
done
