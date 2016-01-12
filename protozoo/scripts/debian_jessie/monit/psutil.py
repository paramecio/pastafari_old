#!/usr/bin/python3

# A script for install alive script 

from subprocess import call

if call("sudo pip3 install psutil",  shell=True) > 0:
    print('Error, cannot create user')
    exit(1)
else:
    print('Installed psutil sucessfully')