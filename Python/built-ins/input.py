#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-12-24 20:01
# @email    : ranchocooper@gmail.com

x, k = map(int, input().split())

# if k == eval(input()):
#     print("True")
#
#  don't konw what's wrong
#
print(eval('{} == {}'.format(input(), k)))
