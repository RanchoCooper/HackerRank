#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-24 22:48
# @email    : ranchocooper@gmail.com


n = int(input())
width = len("{0:b}".format(n))

for i in range(1, n + 1):
    print("{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}".format(i, width=width))

# more: https://pyformat.info/
