#!/usr/bin/python3

from settings import config
from paramecio.citoplasma.mtemplates import ptemplate
from paramecio.citoplasma.lists import SimpleList
from modules.pastafari.models import servers
from paramecio.citoplasma.urls import make_url

def admin(t):
    
    t=ptemplate(__file__)
    
    server=servers.ServerModel()
    url=make_url(config.admin_folder+'/pastafari/servers')
    server_list=SimpleList(server, url, t)
    
    return t.load_template('servers.phtml', server_list=server_list, url=url)