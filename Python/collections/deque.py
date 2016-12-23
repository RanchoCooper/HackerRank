#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-12-23 13:31
# @email    : ranchocooper@gmail.com

from collections import deque

d = deque()

for _ in range(int(input())):
    opt, *args = input().split()
    getattr(d, opt)(*args)

[print(x, end=' ') for x in d]
