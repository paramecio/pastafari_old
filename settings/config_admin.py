#!/usr/bin/python3

from paramecio.citoplasma.i18n import I18n

modules_admin=[[I18n.lang('admin', 'users_admin', 'User\'s Admin'), 'paramecio.modules.admin.admin.ausers', 'ausers']]

modules_other=[I18n.lang('pastafari', 'pastafari', 'Pastafari'), [[I18n.lang('pastafari', 'servers', 'Servers'), 'modules.pastafari.admin.servers', 'pastafari/servers']], 'pastafari']

modules_admin.append(modules_other)

#modules_admin={'ausers': [I18n.lang('admin', 'users_admin', 'User\'s Admin'), 'paramecio.modules.admin.admin.ausers'], 'module_father': [ I18n.lang('common', 'submodule', 'ModuleFather') , {'submodule': ['This is a module', 'paramecio.modules.admin.admin.ausers'] } ] }