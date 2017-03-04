#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2017-03-04 20:10
# @email    : ranchocooper@gmail.com

line = input()

result = sorted(line, key=lambda x: (x.isdigit() and int(x) % 2 == 0, x.isdigit(), x.isupper(), x.islower(), x))

print(*result, sep='')
