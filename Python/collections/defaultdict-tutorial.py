#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-12-02 00:19
# @email    : ranchocooper@gmail.com

from collections import defaultdict
(n, m), r = map(int, input().split()), defaultdict(list)

for i in range(1, n + 1):
    r[input()].append(i)

for _ in range(m):
    c = input()
    print(*r[c] if c in r else [-1])
