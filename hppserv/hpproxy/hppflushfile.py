#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# This file is part of HPProxy (High Performance Proxy)
#
# HPProxy is a proxy engine designed to act mostly transparently to do
# modifications of requests and responses
#
# Copyright (C) 2011 Daniel Rodriguez
#
# You can learn more and contact the author at:
#
#    http://code.google.com/p/hpproxy
#
# HPProxy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HPProxy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with HPProxy. If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
import sys

class FlushFile(object):
    def __init__(self, f):
        self.f = f

    def write(self, x):
        self.f.write(x)
        self.f.flush()

sys.stdout = FlushFile(sys.stdout)
sys.stderr = FlushFile(sys.stderr)
