#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2017-03-04 16:38
# @email    : ranchocooper@gmail.com

def wrapper(func):
    def phone(numbers):
        func('+91 {} {}'.format(number[-10:-5], number[-5:]) for number in numbers)
    return phone

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
