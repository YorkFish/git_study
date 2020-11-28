#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:40:58 2017

@author: jerry_xu
"""
import numpy
from itertools import permutations as pt
comb = pt(range(1,10), 9)

def check(lst):
    return True if sum(lst[0:3]) == sum(lst[3:6]) == sum(lst[6:9]) == sum(lst[0:9:3]) == sum(lst[1:9:3]) == sum(lst[2:9:3]) == sum(lst[0:9:4]) == sum(lst[2:7:2]) else False

i = 0
for each in comb:
    if check(each):
        c = numpy.array(each)
        c = c.reshape((3, 3))
        i += 1
        print 'Number %d :' % i
        print ''
        print c
        print ''
        print '-' * 20
