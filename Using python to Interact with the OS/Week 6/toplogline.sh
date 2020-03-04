#!/usr/bin/env bash
# for mac file location /var/log/system.log
for logfile in /var/log/*log:]; do

  echo "Processing: $logfile"
  cut -d" " -f5- $logfile | sort | uniq -c | sort -nr | head -5
done
