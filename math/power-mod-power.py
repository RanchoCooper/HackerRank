#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-28 16:45
# @email    : ranchocooper@gmail.com

a, b, m = [int(input()) for _ in range(3)]
print(a**b, pow(a, b, m), sep='\n')
