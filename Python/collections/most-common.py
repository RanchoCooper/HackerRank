#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-12-23 19:30
# @email    : ranchocooper@gmail.com

from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
