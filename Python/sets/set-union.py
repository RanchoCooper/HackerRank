#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-28 11:16
# @email    : ranchocooper@gmail.com

_ = input()
a = set(input().split())
_ = input()
b = set(input().split())

print(len(a.union(b)))
