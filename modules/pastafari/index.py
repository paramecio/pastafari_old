#!/usr/bin/python3

from settings import config
from subprocess import Popen, PIPE
from modules.pastafari.models import servers

# Load daemon for monitoritation
"""
python_command='/usr/bin/python3'

if hasattr(config, 'python_command'):
    python_command=config.python_command

args=[python_command+' monit.py']

daemon=Popen(args, bufsize=-1, executable=None, stdin=PIPE, stdout=PIPE, stderr=PIPE, preexec_fn=None, close_fds=True, shell=True, cwd=None, env=None, universal_newlines=True, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=())
"""