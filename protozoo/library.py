#!/usr/bin/python3

import paramiko
import getpass
from protozoo.configclass import ConfigClass

# Prepare keys for ssh connection
def prepare_ssh_keys(password, num_tries=0, yes_pass=True):
    
    try:
        
        rsa=paramiko.RSAKey.from_private_key_file(ConfigClass.private_key, password)
        
    except (paramiko.ssh_exception.PasswordRequiredException, paramiko.ssh_exception.SSHException):
    
        num_tries+=1
    
        if num_tries<4 and yes_pass==True:
        
            p=getpass.getpass('Password for your ssh key:')
            
            rsa=prepare_ssh_keys(p, num_tries)
        
        else:
        
            print(Style.BRIGHT+Fore.WHITE+Back.RED+"This private key need a password if you want execute the tasks...")
        
            return None
    
    return rsa