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

import urllib.parse as urlparse

http_debug_file_name = 'http.debug'


# -----------------------------------------------------------------------
# tests client's header for correctness
def test_client_http_header(header_str):
    ""
    request = header_str.split('\012')[0]
    parts = request.split()

    # we have to have at least 3 words in the request
    # poor check
    if len(parts) < 3:
        return 0
    else:
        return 1


# -----------------------------------------------------------------------
# tests server's response header for correctness
def test_server_http_header(header_str):
    ""
    response = header_str.split('\012'.encode())[0]
    parts = response.split()

    # we have to have at least 2 words in the response
    # poor check
    if len(parts) < 2:
        return 0
    else:
        return 1


# -----------------------------------------------------------------------
def extract_http_header_str(buffer):
    ""
    # let's remove possible leading newlines
    t = buffer.lstrip().encode() if isinstance(buffer, str) else buffer.lstrip()

    # searching for the RFC header's end
    delimiter = '\015\012\015\012'.encode()
    header_end = t.find(delimiter)

    if header_end < 0:
        # may be it is defective header made by junkbuster
        delimiter = '\012\012'.encode()
        header_end = t.find(delimiter)

    if header_end >= 0:
        # we have found it, possibly
        ld = len(delimiter)
        header_str = t[0:header_end + ld]

        # Let's check if it is a proper header
        if test_server_http_header(header_str) or test_client_http_header(header_str):
            # if yes then let's do our work
            if (header_end + ld) >= len(t):
                rest_str = ''
            else:
                rest_str = t[header_end + ld:]
        else:
            # if not then let's leave the buffer as it is
            # NOTE: if there is some junk before right header we will never
            # find that header. Till timeout, I think. Not that good solution.
            header_str = ''
            rest_str = buffer

    else:
        # there is no complete header in the buffer
        header_str = ''
        rest_str = buffer

    return (header_str, rest_str)


# -----------------------------------------------------------------------
def extract_server_header(buffer):
    ""
    header_str, rest_str = extract_http_header_str(buffer)
    if header_str:
        header_obj = HTTP_SERVER_HEAD(header_str)
    else:
        header_obj = None

    return (header_obj, rest_str)


# -----------------------------------------------------------------------
def extract_client_header(buffer):
    ""
    header_str, rest_str = extract_http_header_str(buffer)
    if header_str:
        header_obj = HTTP_CLIENT_HEAD(header_str)
    else:
        header_obj = None

    return (header_obj, rest_str)


# -----------------------------------------------------------------------
def capitalize_value_name(str):
    """"""
    if isinstance(str, bytes):
        str = str.decode()
    tl = str.split('-')
    for i in range(len(tl)):
        tl[i] = tl[i].capitalize()

    return '-'.join(tl)


# -----------------------------------------------------------------------
# some helper classes
# -----------------------------------------------------------------------
class HTTP_HEAD:
    """"""
    pass

    # -------------------------------
    def __init__(self, head_str):
        ""
        self.head_source = ''
        self.params = None
        self.fields = None
        self.order_list = []

        self.head_source = head_str
        head_str = head_str.strip()
        records = head_str.split('\012'.encode())

        # Dealing with response line
        # fields = string.split(records[0], ' ', 2)
        t = records[0].strip().split()
        fields = t[:2] + [''.encode().join(t[2:])]

        self.fields = []
        for i in fields:
            self.fields.append(i.strip())

        # Dealing with params
        params = {}
        order_list = []
        for i in records[1:]:
            parts = i.decode().strip().split(':', 1)
            pname = parts[0].strip().lower()
            if pname not in params:
                params[pname] = []
                order_list.append(pname.lower())
            try:
                params[pname].append(parts[1].strip())
            except:
                msg = "ERROR: Exception in head parsing. ValueName: '%s'" % pname
                # print msg
                self.debug(msg)

        self.params = params
        self.order_list = order_list

    # -------------------------------
    def debug(self, message):
        """"""
        try:
            f = open(http_debug_file_name, 'a')
            f.write(message)
            f.write('\n=====\n')
            f.write(self.head_source)
            f.close()
        except IOError:
            pass
            # Yes, yes, I know, this is just sweeping it under the rug...
            # TODO: implement a persistent filehandle for logging debug messages to.

    # -------------------------------
    def copy(self):
        """"""
        import copy
        return copy.deepcopy(self)

    # -------------------------------
    def get_param_values(self, param_name):
        ""
        param_name = param_name.lower()
        print("Params:", self.params)
        if param_name in self.params:
            return self.params[param_name]
        else:
            return []

    # -------------------------------
    def del_param(self, param_name):
        """"""
        param_name = param_name.lower()
        if param_name in self.params:
            del self.params[param_name]

    # -------------------------------
    def has_param(self, param_name):
        """"""
        param_name = param_name.lower()
        return param_name in self.params

    # -------------------------------
    def add_param_value(self, param_name, value):
        """"""
        param_name = param_name.lower()
        if param_name not in self.params:
            self.params[param_name] = []
        if param_name not in self.order_list:
            self.order_list.append(param_name)
        self.params[param_name].append(value)

    # -------------------------------
    def replace_param_value(self, param_name, value):
        """"""
        self.del_param(param_name)
        self.add_param_value(param_name, value)

    # -------------------------------
    def __repr__(self, delimiter='\n'):
        """"""
        res = ''
        cookies = ''
        res = ' '.encode().join(self.fields) + '\n'.encode()

        for i in self.order_list:
            if i in self.params:
                if i == 'cookie':
                    for k in self.params[i]:
                        cookies = cookies + capitalize_value_name(i) + ': ' + k + '\n'
                else:
                    for k in self.params[i]:

                        # print(type(i))
                        # print(type(res), type(capitalize_value_name(i)), type(k))
                        if isinstance(k, str):
                            k = k.encode()
                        res = res + capitalize_value_name(i).encode() + ': '.encode() + k + '\n'.encode()
        res = res + cookies.encode()
        res = res + '\n'.encode()

        return res

    # -------------------------------
    def send(self, socket):
        """"""
        # """
        res = ''
        cookies = ''
        res = ' '.encode().join(self.fields) + '\015\012'.encode()

        for i in self.order_list:
            if i in self.params:
                if i == 'cookie':
                    for k in self.params[i]:
                        cookies = cookies + capitalize_value_name(i) + ': ' + k + '\015\012'
                else:
                    for k in self.params[i]:
                        res += capitalize_value_name(i).encode() if isinstance(capitalize_value_name(i),
                                                                               str) else capitalize_value_name(i)
                        res += ': '.encode()
                        res += k.encode() if isinstance(k, str) else k
                        res += '\015\012'.encode()
        res = res + cookies.encode()
        res = res + '\015\012'.encode()
        # """
        # res = self.__repr__('\015\012')
        # NOTE!!! 0.9.1 worked, 0.9.5 and 0.9.7 did not with MSN Messenger.
        # We had problem here that prevent MSN Messenger from working.
        # Some work is needed to make __rerp__ working instead of current code..
        try:
            # socket.send(self.head_source)
            socket.send(res)
            # self.debug(res)
            return 1
        except:
            return 0


# -----------------------------------------------------------------------
class HTTP_SERVER_HEAD(HTTP_HEAD):

    # -------------------------------
    def get_http_version(self):
        """"""
        return self.fields[0]

    # -------------------------------
    def get_http_code(self):
        """"""
        return self.fields[1]

    # -------------------------------
    def get_http_message(self):
        ""
        return self.fields[2]


# -----------------------------------------------------------------------
class HTTP_CLIENT_HEAD(HTTP_HEAD):

    # -------------------------------
    def get_http_version(self):
        """"""
        return self.fields[2]

    # -------------------------------
    def get_http_method(self):
        """"""
        return self.fields[0]

    # -------------------------------
    def get_http_url(self):
        """"""
        return self.fields[1]

    # -------------------------------
    def set_http_url(self, new_url):
        """"""
        self.fields[1] = new_url

    # -------------------------------
    # There is some problem with www request header...
    # not all servers want to answer to requests with full url in request
    # but want have net location in 'Host' value and path in url.
    def make_right_header(self):
        ""
        url_tuple = urlparse.urlparse(self.get_http_url())
        net_location = url_tuple[1]
        self.replace_param_value('Host', net_location)

        path = urlparse.urlunparse(tuple([''.encode(), ''.encode()] + list(url_tuple[2:])))
        self.set_http_url(path)

    # -------------------------------
    def get_http_server(self):
        ""
        # trying to get host from url
        url_tuple = urlparse.urlparse(self.get_http_url())
        net_location = url_tuple[1]

        # if there was no host in url then get it from 'Host' value
        if not net_location:
            net_location = self.get_param_values('Host')[0]

        if not net_location:
            net_location = 'localhost'

        # trying to parse user:passwd@www.some.domain:8080
        # is it needed?
        if '@' in net_location:
            cred, net_location = net_location.split('@')
        if ':' in net_location:
            server, port = net_location.split(':')
            port = int(port)
        else:
            server = net_location
            port = 80

        return server, port
