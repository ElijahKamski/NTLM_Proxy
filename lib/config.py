server_config = {'GENERAL':
                     {'LISTEN_PORT': '5865',
                      'PARENT_PROXY': '127.0.0.1',
                      'PARENT_PROXY_PORT': '1254',
                      'PARENT_PROXY_TIMEOUT': '15',
                      'ALLOW_EXTERNAL_CLIENTS': '0',
                      'FRIENDLY_IPS': '',
                      'URL_LOG': '0',
                      'MAX_CONNECTION_BACKLOG': '5',
                      'VERSION': '0.9.9.0.1'
                      },
                 'CLIENT_HEADER':
                     {'Accept': 'image/gif, image/x-xbitmap,'
                                ' image/jpeg, image/pjpeg, application/vnd.ms-excel,'
                                ' application/msword, application/vnd.ms-powerpoint, */*',
                      'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)'},
                 'NTLM_AUTH':
                     {'NT_HOSTNAME': '',
                      'NT_DOMAIN': 'some',
                      'USER': 'admin',
                      'PASSWORD': 'pass',
                      'LM_PART': '1',
                      'NT_PART': '0',
                      'NTLM_FLAGS': '06820000',
                      'NTLM_TO_BASIC': '0'},
                 'DEBUG': {'DEBUG': '0',
                           'BIN_DEBUG': '0',
                           'SCR_DEBUG': '0',
                           'AUTH_DEBUG': '0'}}
