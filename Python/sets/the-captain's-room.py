#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-28 12:04
# @email    : ranchocooper@gmail.com

k, a = int(input()), list(map(int, input().split()))
s = set(a)

print(((sum(s) * k) - (sum(a))) // (k - 1))
