#!/usr/bin/python3

from settings import config
from paramecio.citoplasma.mtemplates import ptemplate
from paramecio.citoplasma.lists import SimpleList
from paramecio.citoplasma import datetime
from modules.pastafari.models import servers
from paramecio.citoplasma.urls import make_url
from paramecio.citoplasma.httputils import GetPostFiles
from paramecio.citoplasma.i18n import I18n
from paramecio.citoplasma.urls import add_get_parameters
from paramecio.cromosoma.coreforms import SelectForm
import json

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
        
        GetPostFiles.get['show_data']=GetPostFiles.get.get('show_data', '0')
        
        if server_view!=False:
        
            if GetPostFiles.get['show_data']=='0':
    
                return ts.load_template('server_status.phtml', server_view=server_view)
    
            elif GetPostFiles.get['show_data']=='1':
                
                get_c=60
            
                ptemplate.show_basic_template=False
            
                network_status=servers.ServerInfoNet()
                
                c=network_status.select_count()
                
                begin_c=c-get_c
                
                if begin_c<0:
                    
                    begin_c=0
                
                network_status.set_conditions('where server=%s', [server_view['ip']])
                
                network_status.set_order(['date'], ['ASC'])
                
                network_status.set_limit([begin_c, get_c])
                
                network_cur=network_status.select()
                
                #arr_dates=[]
                
                arr_dates={}
                
                for net_info in network_cur:
            
                    arr_dates[net_info['device']]=arr_dates.get(net_info['device'], [])
            
                    net_info['date']=datetime.format_fulldate(net_info['date'])
            
                    arr_dates[net_info['device']].append(net_info)
            
                    #arr_dates.append(arr_date)
            
                arr_final_dates={}
            
                for dev in arr_dates:
                    
                    substract_up=arr_dates[dev][0]['network_up']
                    
                    substract_down=arr_dates[dev][0]['network_down']
                    
                    arr_final_dates[dev]=[]
                    
                    for x in range(1, len(arr_dates[dev])):
                        
                        up=arr_dates[dev][x]['network_up']-substract_up
                        
                        down=arr_dates[dev][x]['network_down']-substract_down
                        
                        arr_final_dates[dev].append({'date': arr_dates[dev][x]['date'], 'network_up': up, 'network_down': down})
                        
                        substract_up=arr_dates[dev][x]['network_up']
                    
                        substract_down=arr_dates[dev][x]['network_down']
                        
                        pass
                    
            
                return json.dumps(arr_final_dates)
    
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
    
    
