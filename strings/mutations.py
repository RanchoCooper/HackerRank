#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-24 21:47
# @email    : ranchocooper@gmail.com

string = input()
offset, new = input().split()
offset = int(offset)

print(string[:offset] + new + string[offset + 1:])

# another:
# how about re-inherit from string types and add setter method
