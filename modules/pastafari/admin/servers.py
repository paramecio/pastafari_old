#!/usr/bin/python3

from settings import config
from paramecio.citoplasma.mtemplates import ptemplate
from paramecio.citoplasma.lists import SimpleList
from modules.pastafari.models import servers
from paramecio.citoplasma.urls import make_url
from paramecio.citoplasma.httputils import GetPostFiles

def admin(t):
    
    t=ptemplate(__file__)
    
    GetPostFiles.obtain_get()
    
    GetPostFiles.get['op']=GetPostFiles.get.get('op', '')
    
    server=servers.ServerModel()
    url=make_url(config.admin_folder+'/pastafari/servers')
    
    if GetPostFiles.get['op']=='add_new_server':
    
        server.create_forms()
    
        return ""
        pass
    
    else:
    
        server_list=SimpleList(server, url, t)
    
        return t.load_template('servers.phtml', server_list=server_list, url=url)