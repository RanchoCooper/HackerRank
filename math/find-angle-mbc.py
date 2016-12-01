#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-28 16:18
# @email    : ranchocooper@gmail.com

import math

ab, bc = float(input()), float(input())

print(str(int(round(math.degrees(math.atan2(ab, bc))))) + '°')

# math.degrees: Convert angle x from radians to degrees
# math.atan2: Return the arc tangent (measured in radians) of y/x
