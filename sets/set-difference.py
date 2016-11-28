#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-28 11:49
# @email    : ranchocooper@gmail.com

_, a, _, b = [set(input().split()) for _ in range(4)]

print(len(a - b))
