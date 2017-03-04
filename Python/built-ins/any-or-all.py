#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-12-24 23:13
# @email    : ranchocooper@gmail.com

# input()
# data = input().split()
# if all(map(lambda x: x >= 0, map(int, data))) and any(map(lambda x: x == x[::-1], data)):
#         print("True")
# else:
#     print("False")

_, n = input(), input().split()

print(all([int(x) > 0 for x in n]) and any([x == x[::-1] for x in n]))
