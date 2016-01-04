#!/usr/bin/python3

from paramecio.cromosoma.webmodel import WebModel
from paramecio.cromosoma import corefields
from paramecio.cromosoma.extrafields import ipfield
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

        self.register(corefields.CharField('os_codename'))

        self.register(ipfield.IpField('ip'), True)

        self.register(corefields.CharField('hostname'))

        self.register(corefields.CharField('name'))

        self.register(corefields.CharField('type'))

        self.register(corefields.CharField('profile'))

        self.register(StatusField('status'))
        
