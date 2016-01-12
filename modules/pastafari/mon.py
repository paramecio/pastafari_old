#!/usr/bin/python3

from modules.pastafari.models import servers
from paramecio.citoplasma import datetime
from settings import config
from bottle import get
import json

@get('/pastafari/monit/up/<token>/<ip>')
def index(token, ip):
    
    if config.api_key==token and config.api_key!='':
    
        now=datetime.now()
    
        servermodel=servers.Server()
        
        servermodel.create_forms()
        
        servermodel.reset_require()
        
        servermodel.conditions=['WHERE ip=%s', ip]
        
        servermodel.update({'status': 1, 'last_updated': now})
    
        return "Updated server"
    
    return "Nothing to see here"


@post('/pastafari/monit/info/<token>/<ip>')
def info(token, ip):
    
    pass
