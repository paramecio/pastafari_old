#!/usr/bin/python3

import argparse
import paramiko
import ipaddress
import json
import traceback
from os import getpid,getenv
from settings import config
from modules.pastafari.models import servers
from protozoo.library import prepare_ssh_keys
from protozoo.configclass import ConfigClass
from uuid import uuid4

# A simple daemon for execute a task in a server from a database and save in database. THe scripts for this daemon need return data in json format.

def make_task(server, task):
    
    pass

def start():
    
    parser = argparse.ArgumentParser(description='An daemon used for make a task in a server.The results are saved in a sql database')

    parser.add_argument('--task', help='The task to execute', required=True)
    parser.add_argument('--ip', help='The ip of server where the task must be done', required=True)
    parser.add_argument('--uuid', help='The uuid for identify this process in database', required=True)
    
    args = parser.parse_args()
    
    servertask=servers.ServerTask()
    
    servertask.create_forms()
    
    pid=getpid()
    
    try:
        
        server=str(ipaddress.ip_address(args.ip))
    
    except:
        
        info={'ERROR': 1, 'CODE_ERROR': 1, 'TXT_ERROR': 'Error: ip not valid', 'STATUS':1}
        
        servertask.insert({'task': args.task, 'uuid': args.uuid, 'status': 1, 'error': 1, 'info': json.dumps(info)})
        
        exit(1)
        
    # Prepare basic configuration
    
    home=getenv("HOME")
    
    if ConfigClass.public_key=='':
    
        ConfigClass.public_key=home+'/.ssh/id_rsa.pub'
    
    if ConfigClass.private_key=='':
    
        ConfigClass.private_key=home+'/.ssh/id_rsa'

    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    
    #Check if the unknown host keys are rejected or not
    
    if ConfigClass.deny_missing_host_key == False:
        
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
    #Prepare ssh keys
    
    rsa=prepare_ssh_keys(ConfigClass.password_key)
    
    if rsa==None:
        exit(1)
    
    try:
    
        ssh.connect(server, port=ConfigClass.port, username=ConfigClass.remote_user, password=None, pkey=rsa, key_filename=ConfigClass.private_key, timeout=None, allow_agent=True, look_for_keys=True, compress=False, sock=None, gss_auth=False, gss_kex=False, gss_deleg_creds=True, gss_host=None, banner_timeout=None)
    
    except paramiko.SSHException as e:
        info={'ERROR': 1, 'CODE_ERROR': 1, 'TXT_ERROR': 'Error: Cannot connect: '+str(e), 'STATUS':1}
        servertask.insert({'task': args.task, 'uuid': args.uuid, 'status': 1, 'error': 1, 'info': json.dumps(info)})
        exit(1)
    
    except paramiko.AuthenticationException as e:
        info={'ERROR': 1, 'CODE_ERROR': 1, 'TXT_ERROR': 'Error: Cannot connect: '+str(e), 'STATUS':1}
        servertask.insert({'task': args.task, 'uuid': args.uuid, 'status': 1, 'error': 1, 'info': json.dumps(info)})
        exit(1)
        
    except paramiko.BadHostKeyException as e:
        info={'ERROR': 1, 'CODE_ERROR': 1, 'TXT_ERROR': 'Error: Cannot connect: '+str(e), 'STATUS':1}
        servertask.insert({'task': args.task, 'uuid': args.uuid, 'status': 1, 'error': 1, 'info': json.dumps(info)})
        exit(1)
        
    except OSError as e:
        info={'ERROR': 1, 'CODE_ERROR': 1, 'TXT_ERROR': 'Error: Cannot connect: '+str(e), 'STATUS':1}
        servertask.insert({'task': args.task, 'uuid': args.uuid, 'status': 1, 'error': 1, 'info': json.dumps(info)})
        exit(1)
        
    except:    
        info={'ERROR': 1, 'CODE_ERROR': 1, 'TXT_ERROR': 'Error: Cannot connect: '+traceback.format_exc(), 'STATUS':1}
        servertask.insert({'task': args.task, 'uuid': args.uuid, 'status': 1, 'error': 1, 'info': json.dumps(info)})
        exit(1)
    

if __name__=='__main__':
    start()
    pass



