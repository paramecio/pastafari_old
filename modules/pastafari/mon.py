#!/usr/bin/python3

from modules.pastafari.models import servers
from settings import config
from bottle import get
import json

@get('/pastafari/monit/up/<ip>/<token>')
def index(ip, token):
    
    if config.api_key==token and config.api_key!='':
    
        servermodel=servers.Server()
        
        servermodel.create_forms()
        
        servermodel.reset_require()
        
        servermodel.conditions=['WHERE ip=%s', ip]
        
        servermodel.update({'status': 1})
    
        return "Updated server"
    
    return "Nothing to see here"


