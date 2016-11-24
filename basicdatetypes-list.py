#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-10-31 19:40
# @email    : ranchocooper@gmail.com

n = input()
r = []

for _ in range(int(n)):
    cmd, *args = input().split()
    if cmd != 'print':
        cmd += "(" + ",".join(args) + ")"
        eval("r." + cmd)
    else:
        print(r)


if __name__ == '__main__':
    pass
