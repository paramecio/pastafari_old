from protozoo.configtask import ConfigAction

CurlAction=ConfigAction()
CurlAction.codename='CUrl'
CurlAction.name='A simple command for get urls'
CurlAction.description='A command used in *nix OS used for access to http servers'
CurlAction.script_path='webservers/clients/curl.sh'
CurlAction.script_interpreter='sh'
CurlAction.parameters=''
CurlAction.extra_files=[]

