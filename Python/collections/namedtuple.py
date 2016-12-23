#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-12-02 01:08
# @email    : ranchocooper@gmail.com

n, m = int(input()), input().split().index('MARKS')

print((sum([int(input().split()[m]) for _ in range(n)])) / n)
