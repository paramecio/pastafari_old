#!/usr/bin/python3

from paramecio.cromosoma.webmodel import WebModel
from paramecio.cromosoma import corefields
from paramecio.cromosoma.extrafields import ipfield, datefield
from paramecio.citoplasma import datetime
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
            

class LastUpdatedField(datefield.DateField):        
    
    def __init__(self, name):
        
        super().__init__(name)
        
        self.escape=False
    
    def show_formatted(self, value):
        
        now=datetime.now(gmt=True)
        
        timestamp_now=datetime.obtain_timestamp(now)
        
        timestamp_value=datetime.obtain_timestamp(value)

        five_minutes=int(timestamp_now)-300
        
        if timestamp_value<five_minutes:
            
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
        
        self.register(LastUpdatedField('last_updated'))

        self.register(StatusField('status'))

# {"device_info": {"vboxnet0": [10583, 0], "wlan0": [8116702, 159213180], "eth0": [0, 0], "lo": [495999, 495999]}, "cpu_info": [7.1, 6.0, 5.0, 6.0]}
""""        
class ServerInfo(WebModel):
    
    def create_fields(self):

        self.register(ipfield.IpField('server'), True)

        self.register(corefields.IntegerField('network_up'), True)
        
        self.register(corefields.IntegerField('network_down'), True)
        
        self.register(corefields.FloatField('cpu_use'), True)
"""

class ServerInfoNet(WebModel):
    
    def create_fields(self):
        
        self.register(ipfield.IpField('server'), True)
        
        self.fields['server'].indexed=True
        
        self.register(corefields.CharField('device', 25), True)
        
        self.register(corefields.IntegerField('network_up'), True)
        
        self.register(corefields.IntegerField('network_down'), True)
        
        self.register(datefield.DateField('date'))
        
        
class ServerInfoCPU(WebModel):
    
    def create_fields(self):
        
        self.register(ipfield.IpField('server'), True)
        
        self.fields['server'].indexed=True

        self.register(corefields.FloatField('cpu_use'))
        
        self.register(datefield.DateField('date'), True)

    
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
        
        

