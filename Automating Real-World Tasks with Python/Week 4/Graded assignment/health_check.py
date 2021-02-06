#!/usr/bin/env python3
import shutil
import psutil
import emails

def check_disk_space(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage > 80

def check_memory_usage():
    du = psutil.virtual_memory()
    return du.free < 500 * 1024

def check_localhost():
    return None

if check_cpu_usage():
    subject = "Error - CPU usage is over 80%"
elif check_disk_space("/"):
    subject = "Error - Available disk space is less than 20%"
elif check_memory_usage():
    subject = "Error - Available memory is less than 500MB"
elif check_localhost():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
email_title = subject
body = "Please check your system and resolve the issue as soon as possible."
message = emails.generate_erro_mail(sender, receiver, title, body)
emails.send_email(message)
