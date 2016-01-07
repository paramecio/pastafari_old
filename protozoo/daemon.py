#!/usr/bin/python3

import argparse
import paramiko
import ipaddress
import json
import traceback
from os import getpid,getenv,path
from importlib import import_module
from settings import config
from modules.pastafari.models import servers
from protozoo.library import prepare_ssh_keys
from protozoo.configclass import ConfigClass
from protozoo.configtask import ConfigTask
from uuid import uuid4

# A simple daemon for execute a task in a server from a database and save in database. THe scripts for this daemon need return data in json format.

def make_task(server, task):
    
    pass

def start():
    
    parser = argparse.ArgumentParser(description='An daemon used for make a task in a server.The results are saved in a sql database')

    parser.add_argument('--task', help='The task to execute', required=True)
    parser.add_argument('--id', help='The id of server where the task must be done', required=True)
    parser.add_argument('--uuid', help='The uuid for identify this process in database', required=True)
    
    info={}
    
    args = parser.parse_args()
    
    servertask=servers.ServerTask()
    
    servertask.create_forms()
    
    server=servers.Server()
    
    pid=getpid()
    
    #servertask.conditions=['where id=%s', [args.id]]
    
    arr_server=server.select_a_row(args.id)
    
    if arr_server==False:
        
        info={'ERROR': 1, 'CODE_ERROR': 4, 'TXT_ERROR': 'Error: server not exists', 'STATUS':1}
        
        servertask.insert({'task': args.task, 'uuid': args.uuid, 'status': 1, 'error': 1, 'pid': pid, 'info': json.dumps(info)})
        
        exit(1)
    
    arr_server['ip']=arr_server.get('ip', '')
    
    if arr_server['ip']=='':
        info={'ERROR': 1, 'CODE_ERROR': 2, 'TXT_ERROR': 'Error: server not exists', 'STATUS':1}
        
        servertask.insert({'task': args.task, 'uuid': args.uuid, 'status': 1, 'error': 1, 'pid': pid, 'info': json.dumps(info)})
        
        exit(1)
    
    ip=arr_server['ip']
    
    try:
        
        server=str(ipaddress.ip_address(ip))
    
    except:
        
        info={'ERROR': 1, 'CODE_ERROR': 1, 'TXT_ERROR': 'Error: ip not valid', 'STATUS':1}
        
        servertask.insert({'task': args.task, 'uuid': args.uuid, 'status': 1, 'error': 1, 'pid': pid, 'info': json.dumps(info)})
        
        exit(1)

    # Prepare basic configuration
    
    home=getenv("HOME")
    
    if ConfigClass.public_key=='':
    
        ConfigClass.public_key=home+'/.ssh/id_rsa.pub'
    
    if ConfigClass.private_key=='':
    
        ConfigClass.private_key=home+'/.ssh/id_rsa'

    # Prepare task
    
    task_name=path.basename(args.task)
    
    task=args.task.replace('.','_')
    
    task=args.task.replace('/','.')
    
    #Seeking task path
    
    for p in ConfigClass.tasks_path:
        
        task_path=p+'.'+task+'.config'
        
        task_path_route=task_path.replace('.','/')+'.py'
        
        #tpath=Path(task_path_route)
        
        if path.isfile(task_path_route):
            break
    try:
        
        config_task=import_module(task_path)
        
    except SyntaxError as e:
        
        info={'ERROR': 1, 'CODE_ERROR': 1, 'TXT_ERROR': 'Error: error in task: '+str(e), 'STATUS':1}
        servertask.insert({'task': args.task, 'uuid': args.uuid, 'status': 1, 'error': 3, 'info': json.dumps(info)})
        
        exit(1)
    except:
        info={'ERROR': 1, 'CODE_ERROR': 1, 'TXT_ERROR': 'Error: error in task: '+traceback.format_exc(), 'STATUS':1}
        servertask.insert({'task': args.task, 'uuid': args.uuid, 'status': 1, 'error': 1, 'info': json.dumps(info)})
        exit(1)
        
    # Load locals
    
    

    # Prepare ssh connection

    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    
    #Check if the unknown host keys are rejected or not
    
    if ConfigClass.deny_missing_host_key == False:
        
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
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
    
    # Check that exists the script in server
    
    if len(ConfigTask.action)==0:
        logging.warning('Error, check your task. The number of actions in task is zero')
        exit(1)
    
    for action in ConfigTask.action:
        
        # Check if exists the files
        
        path_file='protozoo/scripts/'+arr_server['os_codename']+'/'+action.script_path
        
        stdin, stdout, stderr = ssh.exec_command('if [ ! -f "'+path_file+'" ] ; then false ; fi')
        
        if stdout.channel.recv_exit_status()>0:
            # Uploading the files first time if not exists
            # TODO Use md5 hash for check the file.
            # print('File '+path_file+' doesn\'t exists')
            # Upload the script of this task

if __name__=='__main__':
    start()
    pass



