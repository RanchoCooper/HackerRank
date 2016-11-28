#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-28 12:13
# @email    : ranchocooper@gmail.com

for _ in range(int(input())):
    _, a, _, b = [set(map(int, input().split())) for _ in range(4)]
    print(a < b)
