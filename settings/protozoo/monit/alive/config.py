#!/usr/bin/python3 

from protozoo.tasks.monit.alive import config

def add_data(server_data):
    
    config.AliveAPIAction.parameters='--user=pzoo --url="http://192.168.1.79:8080/pastafari/monit/up/83d89ec9ad381579e1f57eb416a2541806a90e69cdb791672fe98dc350b58042d5784b0894a8d2b9e7bc02bd86663be1ad6a9d01b1ee926a634f5fe9e4d956f0/'+server_data['ip']+'"'