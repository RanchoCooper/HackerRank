#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-24 22:01
# @email    : ranchocooper@gmail.com

string, substr, count = input(), input(), 0

for c in range(len(string)):
    if string[c:c+len(substr)] == substr:
        count += 1

print(count)
