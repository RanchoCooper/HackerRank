#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-10-25 19:20
# @email    : ranchocooper@gmail.com

from itertools import product

a = list(map(int, input.split()))
b = list(map(int, input.split()))

print(*list(product(a, b)))
