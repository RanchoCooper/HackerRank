#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-12-23 19:40
# @email    : ranchocooper@gmail.com

import calendar

m, d, y = map(int, input().split())

print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())

