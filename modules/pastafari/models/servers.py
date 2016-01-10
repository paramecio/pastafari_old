#!/usr/bin/python3

from paramecio.cromosoma.webmodel import WebModel
from paramecio.cromosoma import corefields
from paramecio.cromosoma.extrafields import ipfield, datefield
from paramecio.citoplasma.urls import make_media_url_module
"""
class ServerType(WebModel):
    
    def create_fields(self):
        
        self.register(corefields.CharField('name', 255), True)
        self.register(corefields.CharField('codename', 255), True)

class ServerOs(WebModel):
    
    def create_fields(self):
        
        self.register(corefields.CharField('name', 255), True)
        self.register(corefields.CharField('codename', 255), True)

class NodeModel(WebModel):

    def create_fields(self):

        self.register(corefields.CharField('hostname', 255), True)
        
        self.register(ipfield.IpField('ip'), True)
      
"""

class StatusField(corefields.BooleanField):
    
    def __init__(self, name, size=1):
        
        super().__init__(name, size)
        
        self.escape=False
    
    def show_formatted(self, value):
        
        if value==0:
            
            return '<img src="'+make_media_url_module('images/status_red.png', 'pastafari')+'" />'
        else:
            return '<img src="'+make_media_url_module('images/status_green.png', 'pastafari')+'" />'
            
        

class Server(WebModel):

    def create_fields(self):

        self.register(corefields.CharField('os_codename'), True)

        self.register(ipfield.IpField('ip'), True)

        self.register(corefields.CharField('hostname'), True)

        self.register(corefields.CharField('name'), True)

        self.register(corefields.CharField('type'), True)

        self.register(corefields.CharField('profile'), True)
        
        self.register(datefield.DateField('last_updated'))

        self.register(StatusField('status'))
        
class ServerTask(WebModel):
    
    def create_fields(self):
        
        self.register(corefields.CharField('task'))
        
        self.register(corefields.CharField('uuid'))
        
        self.register(corefields.BooleanField('status'))
        
        self.register(corefields.TextField('info'))
        
        self.register(corefields.IntegerField('pid'))
        

class ServerMonit(WebModel):
    
    def create_fields(self):
        
        self.register(corefields.CharField('check_task'), True)
        
        self.register(corefields.CharField('profile'))
        
        
    
