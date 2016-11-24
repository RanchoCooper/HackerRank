#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-24 20:58
# @email    : ranchocooper@gmail.com


n = int(input())
d = {}
# d = {
#   'name': [1, 2, 3],
#   ....
# }

for _ in range(n):
    name, *score = input().split()
    d[name] = [int(x) for x in score]

theone = input()
print("%.2f" % (sum(d[theone])/3))

# tips:
# missing the parentheses in Formatted output!
