#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2017-03-04 17:23
# @email    : ranchocooper@gmail.com

import operator
def person_lister(f):
    def inner(people):
        return (f(person) for person in sorted(people, key=operator.itemgetter(2)))
    return inner

@person_lister
def name_format(info):
    return ' '.join(["Mr." if info[3] == "M" else "Ms.", info[0], info[1]])

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
