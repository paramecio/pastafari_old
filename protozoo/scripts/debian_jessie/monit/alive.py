#!/usr/bin/python3

# A script for install alive script 

import argparse
import re
import socket
from subprocess import call

parser = argparse.ArgumentParser(description='A script for install alive script and cron')

parser.add_argument('--url', help='The url where notify that this server is alive', required=True)
parser.add_argument('--user', help='The user for pastafari', required=True)

args = parser.parse_args()

url=args.url

check_url = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

if check_url.match(args.url):
    
    # Need obtain ip of this shit
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com",80))
    ip=s.getsockname()[0]
    s.close()
    
    # Edit alive cron 
    
    f=open('protozoo/scripts/debian_jessie/monit/files/crontab/alive')
    
    alive_cron=f.read()
    
    f.close()
    
    alive_cron=alive_cron.replace('/home/spanel/protozoo/scripts/debian_jessie/monit/files/alive.py', '/home/'+args.user+'/protozoo/scripts/debian_jessie/monit/files/alive.py')
    
    f=open('protozoo/scripts/debian_jessie/monit/files/crontab/alive', 'w')
    
    f.write(alive_cron)
    
    f.close()
    
    # Edit alive script
    
    f=open('protozoo/scripts/debian_jessie/monit/files/alive.py')
    
    alive_script=f.read()
    
    f.close()
    
    alive_script=alive_script.replace("url='http://url/to/server'", "url='"+args.url+"'")
    
    f=open('protozoo/scripts/debian_jessie/monit/files/alive.py', 'w')
    
    f.write(alive_script)
    
    f.close()
    
    # Copy cron alive to /etc/cron.d/
    
    if call("sudo cp protozoo/scripts/debian_jessie/monit/files/crontab/alive /etc/cron.d/alive", shell=True) > 0:
        print('Error, cannot install config.py file')
        exit(1)
    else:
        print('Added config.py for config paramecio')
    
    print('Script installed successfully')
    
    exit(0)
    
else:
    
    print('Error installing the module')
    
    exit(1)
    
