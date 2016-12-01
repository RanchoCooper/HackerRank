#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-28 16:42
# @email    : ranchocooper@gmail.com

a, b = int(input()), int(input())

print(a // b, a % b, divmod(a, b), sep='\n')
