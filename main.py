#! /usr/bin/python

import sys

from lib import config, config_affairs, server

# This file is part of 'NTLM Authorization Proxy Server'
# Copyright 2001 Dmitry A. Rozmanov <dima@xenon.spb.ru>
#
# NTLM APS is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# NTLM APS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with the sofware; see the file COPYING. If not, write to the
# Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
#
import __init__
from lib.U32 import U32

# --------------------------------------------------------------
# config affairs
# look for default config name in lib/config.py
conf = config.read_config(config.findConfigFileNameInArgv(sys.argv, __init__.ntlmaps_dir + '/'))

conf['GENERAL']['VERSION'] = '0.9.9.0.1'

# --------------------------------------------------------------
print('NTLM authorization Proxy Server v%s' % conf['GENERAL']['VERSION'])
print('Copyright (C) 2001-2004 by Dmitry Rozmanov and others.')

config = config_affairs.arrange(conf)

# --------------------------------------------------------------
# let's run it
print(U32())
a = U32()
a+=1
print(a)
serv = server.AuthProxyServer(config)
serv.run()
