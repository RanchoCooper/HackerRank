#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-28 16:28
# @email    : ranchocooper@gmail.com

for i in range(1, int(input()) + 1):
    print(((10**i-1)//9)**2)

# 1*1=1
# 11*11=121
# 111*111=12321
# ...
# ((10^2-1)//9)^2 == 123..i...321
