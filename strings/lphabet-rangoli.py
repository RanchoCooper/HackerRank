#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-24 22:56
# @email    : ranchocooper@gmail.com

import string
alpha = string.ascii_letters

n = int(input())
l = []

for i in range(n):
    s = '-'.join(alpha[i:n])
    l.append((s[::-1]+s[1:]).center(4*n-3, '-'))

print('\n'.join(l[:0:-1] + l))
