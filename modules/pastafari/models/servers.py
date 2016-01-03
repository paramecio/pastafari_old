#!/usr/bin/python3

from paramecio.cromosoma.webmodel import WebModel
from paramecio.cromosoma import corefields
from paramecio.cromosoma.extrafields import ipfield

class ServerType(WebModel):
    
    def create_fields(self):
        
        self.register(corefields.CharField('name', 255), True)
        self.register(corefields.CharField('codename', 255), True)

class ServerOs(WebModel):
    
    def create_fields(self):
        
        self.register(corefields.CharField('name', 255), True)
        self.register(corefields.CharField('codename', 255), True)

class ServerModel(WebModel):

    def create_fields(self):

        self.register(corefields.CharField('hostname', 255), True)
        
        # The ip should be used for connect to the server
        
        self.register(ipfield.IpField('ip'), True)
        
        self.register(corefields.ForeignKeyField('type', ServerType()), True)
        self.register(corefields.ForeignKeyField('os', ServerOs()), True)