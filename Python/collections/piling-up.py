#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-12-23 13:41
# @email    : ranchocooper@gmail.com

t = int(input())

for _ in range(t):
    input()
    nums = list(map(int, input().split()))
    n, i = len(nums), 0
    while i < n - 1 and nums[i] >= nums[i + 1]:
        i += 1
    while i < n - 1 and nums[i] <= nums[i + 1]:
        i += 1
    print("Yes" if i == n - 1 else "No")
