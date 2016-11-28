#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-28 11:05
# @email    : ranchocooper@gmail.com

n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))

# add `['']` in the eval statment
# ensure that there are always 2 elements at least
