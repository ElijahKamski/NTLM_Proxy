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
# aint with the sofware; see the file COPYING. If not, write to the
# Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
#


C = 0x1000000000


def norm(n):
    return n & 0xFFFFFFFF


class U32:
    # self = 0

    def __init__(self, value=0):
        self.v = C + norm(abs(int(value)))

    def set(self, value=0):
        self.v = C + norm(abs(int(value)))

    def __repr__(self):
        return hex(norm(self.v))

    def __int__(self):
        return int(norm(self.v))

    def __chr__(self):
        return chr(norm(self.v))

    def __add__(self, b: int):
        r = U32()
        if isinstance(b, self.__class__):
            r.v = C + norm(self.v + b.v)
        else:
            r.v = C + norm(self.v + b)
        return r

    def __sub__(self, b):
        r = U32()
        if isinstance(b, self.__class__):
            if self.v < b.v:
                r.v = C + norm(0x100000000 - (b.v - self.v))
            else:
                r.v = C + norm(self.v - b.v)
        else:
            if self.v < b:
                r.v = C + norm(0x100000000 - (b - self.v))
            else:
                r.v = C + norm(self.v - b)
        return r

    def __mul__(self, b):
        r = U32()
        if isinstance(b, self.__class__):
            r.v = C + norm(self.v * b.v)
        else:
            r.v = C + norm(self.v * b)
        return r

    def __div__(self, b):
        r = U32()
        if isinstance(b, self.__class__):
            r.v = C + (norm(self.v) / norm(b.v))
        else:
            r.v = C + (norm(self.v) / norm(b))
        return r

    def __mod__(self, b):
        r = U32()
        if isinstance(b, self.__class__):
            r.v = C + (norm(self.v) % norm(b.v))
        else:
            r.v = C + (norm(self.v) % norm(b))
        return r

    def __neg__(self):
        return U32(self.v)

    def __pos__(self):
        return U32(self.v)

    def __abs__(self):
        return U32(self.v)

    def __invert__(self):
        r = U32()
        r.v = C + norm(~self.v)
        return r

    def __lshift__(self, b):
        r = U32()
        if isinstance(b, self.__class__):
            r.v = C + norm(self.v << b.v)
        else:
            r.v = C + norm(self.v << b)
        r.v = C + norm(self.v << b)
        return r

    def __rshift__(self, b):
        r = U32()
        if isinstance(b, self.__class__):
            r.v = C + norm(self.v >> b.v)
        else:
            r.v = C + norm(self.v >> b)
        r.v = C + (norm(self.v) >> b)
        return r

    def __and__(self, b):
        r = U32()
        if isinstance(b, self.__class__):
            r.v = C + norm(self.v & b.v)
        else:
            r.v = C + norm(self.v & b)
        return r

    def __or__(self, b):
        r = U32()
        if isinstance(b, self.__class__):
            r.v = C + norm(self.v | b.v)
        else:
            r.v = C + norm(self.v | b)
        return r

    def __xor__(self, b):
        r = U32()
        if isinstance(b, self.__class__):
            r.v = C + norm(self.v ^ b.v)
        else:
            r.v = C + norm(self.v ^ b)
        return r

    def __not__(self):
        return U32(not norm(self.v))

    def truth(self):
        return norm(self.v)

    def __cmp__(self, b):
        if isinstance(b, self.__class__):
            if norm(self.v) > norm(b.v):
                return 1
            elif norm(self.v) < norm(b.v):
                return -1
            else:
                return 0
        if norm(self.v) > norm(b):
            return 1
        elif norm(self.v) < norm(b):
            return -1
        else:
            return 0

    def __nonzero__(self):
        return norm(self.v)
