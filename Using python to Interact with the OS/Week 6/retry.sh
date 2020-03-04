#!/usr/bin/env bash
n=0
command=$1
while ! $command && [ $n -le 5 ]; do
  #statements
  sleep $n
  ((n=n+1))
  echo "Retry #$n"
done
