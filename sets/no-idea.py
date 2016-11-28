#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-25 20:12
# @email    : ranchocooper@gmail.com

n, m = input().split()
arr = input().split()
a = set(input().split())
b = set(input().split())

print(sum([(i in a) - (i in b) for i in arr]))

# True == 1 and False == 0
