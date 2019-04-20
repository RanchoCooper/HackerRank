#!/usr/bin/env python
# encoding: utf-8

# @author rancho
# @date 2019-04-20

import math
import os


def miniMaxSum(arr):
    sum_ = sum(arr)
    min_ = sum_ - max(arr)
    max_ = sum_ - min(arr)
    print("{} {}".format(min_, max_))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
