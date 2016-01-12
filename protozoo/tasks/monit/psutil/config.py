#!/usr/bin/python3

from protozoo.configtask import ConfigTask, ConfigAction
from protozoo.configtasks.psutil import PyPsutilAction

MonitInfoAction=ConfigAction()
MonitInfoAction.codename='MonitInfo'
MonitInfoAction.name='MonitInfo'
MonitInfoAction.description='An script using psutil python module for send info to a server'
MonitInfoAction.script_path='monit/monit.py'
MonitInfoAction.script_interpreter='python3'
MonitInfoAction.parameters=''
MonitInfoAction.extra_files=['monit/files/crontab/get_info', 'monit/files/get_info.py']

ConfigTask.task='psutilinfo'
ConfigTask.info="A script for send info to a webserver api using psutil python3 module"

ConfigTask.action=[PyPsutilAction, MonitInfoAction]

