#!/usr/bin/python3

import psutil
import json

network_info=psutil.net_io_counters(pernic=True)

network_devices=psutil.net_if_addrs()

cpu_idle=psutil.cpu_percent(interval=1, percpu=True)

dev_info={}

for device, info in network_info.items():
    
    #{'eth0': netio(bytes_sent=485291293, bytes_recv=6004858642, packets_sent=3251564, packets_recv=4787798, errin=0, errout=0, dropin=0, dropout=0),
    
    dev_info[device]=[info[0], info[1]]


#for device, info in network_devices.items():
    
    #print(info)

print(json.dumps({'device_info': dev_info, 'cpu_info': cpu_idle}))

