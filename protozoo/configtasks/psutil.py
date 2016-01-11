#!/usr/bin/python3

from protozoo.configtask import ConfigTask, ConfigAction

PyPsutilAction=ConfigAction()
PyPsutilAction.codename='psutil'
PyPsutilAction.name='PyPsutil'
PyPsutilAction.description='Installing psutil module for python3'
PyPsutilAction.script_path='monit/psutil.py'
PyPsutilAction.script_interpreter='python3'
PyPsutilAction.parameters=''
PyPsutilAction.extra_files=[]