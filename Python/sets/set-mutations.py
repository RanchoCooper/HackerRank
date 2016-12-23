#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-28 11:56
# @email    : ranchocooper@gmail.com

# update() or |=
#   update the set by merging them
# intersection_update() or &=
#   update the set by their intersection
#  difference_update() or -=
#  sysmmetric_difference_update() or ^=

n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    command, _ = input().split()
    t = set(map(int, input().split()))
    eval('s.{0}({1})'.format(command, t))

print(sum(s))
