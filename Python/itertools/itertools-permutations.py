#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-10-25 19:27
# @email    : ranchocooper@gmail.com

from itertools import permutations

seq, n = input().split()

for i in permutations(sorted(seq), int(n)):
    print(''.join(i))

# pythonic
print(*[''.join(x) for x in permutations(sorted(seq), int(n))], sep='\n')
# `sep` is the separator for extending unpacking *
