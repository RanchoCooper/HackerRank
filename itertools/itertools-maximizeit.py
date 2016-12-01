#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-10-25 19:49
# @email    : ranchocooper@gmail.com

from functools import reduce   # removed from global namespace in py3

k, m = map(int, input().split())
#klist = [[int(x) for x in input().split()] for i in range(int(k))]
klist = [[int(x) for x in input().split()[1:]] for _ in range(int(k))]
# elements in klist already `int` type

# error: TypeError: 'int' object is not iterable
# reduce(sum, map(lambda x: x*x, [int(max(seq)) for seq in nlist]))

print(reduce(lambda x, y: x+y, map(lambda x: x*x, [max(seq) for seq in klist])) % m)

