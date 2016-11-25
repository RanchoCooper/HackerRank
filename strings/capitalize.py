#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-24 23:10
# @email    : ranchocooper@gmail.com

string = input()

for word in string.split():
    string = string.replace(word, word.capitalize())

# print(input().title())
# wrong-input:
#     12sdf  --> 12Sdf
