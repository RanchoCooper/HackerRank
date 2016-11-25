#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-24 21:24
# @email    : ranchocooper@gmail.com

# inspiration comes from `this.py` module
# d = {}
# for c in (65, 97):
#     for i in range(26):
#         d[chr(i+c)] = chr((i+13) % 26 + c)

# print("".join([d.get(c, c) for c in s]))

s = input()

def translate(char):
    if 65 <= ord(char) <= 90:
        return chr(ord(char) + 32)
    elif 97 <= ord(char) <= 122:
        return chr(ord(char) - 32)
    else:
        return char

def trans(string):
    for x in string:
        print(translate(x), end='')

trans(s)

# tips:
# print(input().swapcase()) ......
