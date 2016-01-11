#!/usr/bin/python3

from protozoo.configtask import ConfigTask, ConfigAction
from protozoo.configtasks.prebuildtask import Python3Action

AliveAPIAction=ConfigAction()
AliveAPIAction.codename='aliveapi'
AliveAPIAction.name='AliveAPI'
AliveAPIAction.description='An script for say that a server is alive'
AliveAPIAction.script_path='monit/alive.py'
AliveAPIAction.script_interpreter='python3'
AliveAPIAction.parameters=''
AliveAPIAction.extra_files=['monit/files/crontab/alive', 'monit/files/alive.sh']

ConfigTask.task='monit'
ConfigTask.info="A script that say that the server is alive"

ConfigTask.action=[Python3Action, AliveAPIAction]