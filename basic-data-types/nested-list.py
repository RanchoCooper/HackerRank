#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-24 20:44
# @email    : ranchocooper@gmail.com

n = int(input())

sheet = [[input(), float(input())] for _ in range(n)]

second = sorted(list(set([score for name, score in sheet])))[1]

print('\n'.join([name for name, score in sorted(sheet) if score == second]))
