#!/usr/bin/python3

# You need install cromosoma for use this.

from paramecio.cromosoma.webmodel import WebModel

#server_used="wsgiref"

#Host/IP where bind the server

port=8080

debug=True

reloader=True

admin_folder='admin'

host='localhost'

allowed_ips=[]

#The theme by default

theme='default'

#Base directory for save modules

#base_modules="modules"

#Type server used for connect to the internet...

server_used="wsgiref"

#Module showed in index

default_module="welcome"

#Modules with permissions to access for users

modules=['paramecio.modules.welcome', 'paramecio.modules.admin', 'paramecio.modules.lang', 'modules.tests', 'modules.pastafari']

#Activate sessions?

session_enabled=True

#Variables for beaker sessions

cookie_name = 'paramecio.session'

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': False,
    'session.data_dir': './sessions',
    'session.auto': True
}

cache_session_opts = {
    
}

#The base url 

base_url='/'

#Can be absolute or relative

media_url='/'

#SSL support built in server. You need cherrypy installed for use this.

ssl=False

# Cert file for ssl

cert_pem=''

# Key file for ssl

privkey_pem=''

#WARNING: only use this feature in development, not in production.

yes_static=True

#Database mysql config, if you want anything...

#WebModel.connections={'default': {'name': 'default', 'host': 'localhost', 'user': 'root', 'password': '', 'db': 'example', 'charset': 'utf8mb4', 'set_connection': False} }

WebModel.connections={'default': {'name': 'default', 'host': 'localhost', 'user': 'root', 'password': 'sirena', 'db': 'paramecio_db', 'charset': 'utf8mb4', 'set_connection': False} }
