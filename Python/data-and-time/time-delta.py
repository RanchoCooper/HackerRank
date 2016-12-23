#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-12-23 19:59
# @email    : ranchocooper@gmail.com

from datetime import datetime as dt

fmt = '%a %d %b %Y %H:%M:%S %z'

for _ in range(int(input())):
    delta = dt.strptime(input(), fmt) - dt.strptime(input(), fmt)
    print(int(abs(delta).total_seconds()))
