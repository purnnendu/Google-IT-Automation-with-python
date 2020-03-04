#!/usr/bin/env bash
line="----------------------------------------------------------"
echo "Start time: $(date)";echo $line

echo "Uptime";uptime; echo $line

echo "Free Space";free;echo $line

echo "WHO";who;echo $line

echo "End time: $(date)";echo
