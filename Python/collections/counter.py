#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-12-02 00:06
# @email    : ranchocooper@gmail.com

from collections import Counter

_, count, total = input(), Counter(input().split()), 0

for _ in range(int(input())):
    size, price = input().split()
    if count[size]:
        total += int(price)
        count[size] -= 1

print(total)
