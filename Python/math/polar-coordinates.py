#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-28 16:05
# @email    : ranchocooper@gmail.com

"""
    cmath.phase
        return the phase of a complex number
    abs
        return the modules (absolute value) of complex number
"""
from cmath import phase
n = complex(input())
print(abs(n))
print(phase(n))

# @cleanest
# import cmath
# print(*cmath.polar(complex(input))), sep='\n')
