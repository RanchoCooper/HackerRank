#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-12-01 23:45
# @email    : ranchocooper@gmail.com

for i in range(1, int(input())):
    print(i * str(i))

# but the judgement hopes int type

for i in range(1, int(input())):
    print((pow(10, i)//9) * i)
