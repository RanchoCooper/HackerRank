#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-25 09:27
# @email    : ranchocooper@gmail.com

s = input()

vowels = 'AEIOU'

kevsc = 0
stusc = 0

for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s) - i)
    else:
        stusc += (len(s) - i)

if kevsc > stusc:
    print "Kevin", kevsc
elif kevsc < stusc:
    print "Stuart", stusc
else:
    print "Draw"
