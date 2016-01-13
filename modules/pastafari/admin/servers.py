#!/usr/bin/python3

from settings import config
from paramecio.citoplasma.mtemplates import ptemplate
from paramecio.citoplasma.lists import SimpleList
from modules.pastafari.models import servers
from paramecio.citoplasma.urls import make_url
from paramecio.citoplasma.httputils import GetPostFiles
from paramecio.citoplasma.i18n import I18n
from paramecio.citoplasma.urls import add_get_parameters
from paramecio.cromosoma.coreforms import SelectForm

ts=ptemplate(__file__)

def admin(t):
  
    GetPostFiles.obtain_get()
    
    GetPostFiles.get['op']=GetPostFiles.get.get('op', '')
    
    server=servers.Server()
    
    url=make_url(config.admin_folder+'/pastafari/servers')
    
    if GetPostFiles.get['op']=='add_new_server':
    
        #Check if the server can be access with god module using ssh, if yes, install idea(aka virus or platon) using protozoo or similar program
    
        server.create_forms()
    
        return ""
        pass
    elif GetPostFiles.get['op']=='view_status':
        
        GetPostFiles.get['id']=GetPostFiles.get.get('id', '0')
    
        server_id=int(GetPostFiles.get['id'])
    
        server_view=server.select_a_row(server_id)
        
        network_status=servers.ServerInfoNet()
        
        network_status.conditions=['where server=%s', [server_view['ip']]]
        
        network_cur=network_status.select()
        
        if server_view!=False:
    
            return ts.load_template('server_status.phtml', server_view=server_view)
    
    else:
    
        # Obtain uptimes
        
        server.conditions=['where status=%s', [0]]
        
        num_servers_failed=server.select_count()
        
        server.conditions=['where status=%s', [1]]
        
        num_servers_uptime=server.select_count()
        
        # Obtain profiles
        
        server.distinct='DISTINCT'
        
        server.order_by='order by profile ASC'
        
        arr_profiles=server.select_to_array(['profile'])
        
        profiles=SelectForm('profile', '')
        
        profiles.arr_select['']=''
        
        for profile in arr_profiles.values():
            
            profiles.arr_select[profile['profile']]=profile['profile']
    
        server.distinct=''
        
        GetPostFiles.get['profile']=GetPostFiles.get.get('profile', '')
        
        url=add_get_parameters(url, profile= GetPostFiles.get['profile'])
        
        if GetPostFiles.get['profile'] in profiles.arr_select and GetPostFiles.get['profile']!='':
            server.conditions=['where profile=%s', [GetPostFiles.get['profile']]]
        
        profiles.default_value=GetPostFiles.get['profile']
    
        server_list=SimpleList(server, url, t)
        
        #server_list.fields=['id', 'type']
        
        server_list.fields_showed=['hostname', 'ip', 'profile', 'type', 'last_updated']
        
        server_list.yes_search=False
        
        server_list.arr_extra_fields=[I18n.lang('common', 'options', 'Options')]
        
        server_list.arr_extra_options=[server_options]
    
        return ts.load_template('servers.phtml', server_list=server_list, url=url, profiles=profiles, num_servers_failed=num_servers_failed, num_servers_uptime=num_servers_uptime)
    
def server_options(url, id, arr_row):
        options=[]
        options.append('<a href="'+add_get_parameters(url, op='view_status', id=id)+'">'+I18n.lang('pastafari', 'view_status', 'View status')+'</a>')
        return options
    
    