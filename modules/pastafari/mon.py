#!/usr/bin/python3

from modules.pastafari.models import servers
from paramecio.citoplasma import datetime
from paramecio.citoplasma.httputils import GetPostFiles
from settings import config
from bottle import get, post
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
    
    if config.api_key==token and config.api_key!='':
    
        now=datetime.now()
    
        GetPostFiles.obtain_post()
    
        servermodel=servers.Server()
        
        servermodel.conditions=['WHERE ip=%s', [ip]]
        
        arr_server=servermodel.select_a_row_where()
        
        arr_server['id']=arr_server.get('id', 0)
        
        if arr_server['id']!=0:
            
            servernet=servers.ServerInfoNet()
            
            servercpu=servers.ServerInfoCPU()
            
            #{"device_info": {"eth0": [0, 0], "lo": [593521, 593521], "wlan0": [21354106, 376953085], "vboxnet0": [10847, 0]}, "cpu_info": 6.1}
            
            try:
                
                GetPostFiles.post['data_json']=GetPostFiles.post.get('data_json', '')
                
                info=json.loads(GetPostFiles.post['data_json'])
                
                #print(info)
                
                if type(info).__name__=='dict':
                    #print('pepe')
                    info['cpu_info']=info.get('cpu_info', 0)
                    
                    servercpu.create_forms()
                    
                    if servercpu.insert({'server': ip, 'cpu_use': info['cpu_info'], 'date': now}):
                        
                        print('Done')
                    else:
                        
                        print(servercpu.fields_errors)
                        
                    info['net_info']=info.get('net_info', {})

                    servernet.create_forms()

                    for dev, data in info['net_info'].items():
                        
                        servernet.insert({'server': ip, 'device': dev, 'network_up': data[0], 'network_down': data[1], 'date': now})
                    
                    
            except:
                
                return 'Error'
            
            #for 
            
            #print(GetPostFiles.post['data_json'])
            
    
    pass
