#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-12-24 22:58
# @email    : ranchocooper@gmail.com

n, m = map(int, input().split())

rows = [input() for _ in range(n)]
k = int(input())

for row in sorted(rows, key=lambda row: int(row.split()[k])):
    print(row)
