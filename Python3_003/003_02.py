#!/usr/bin/env python3
# coding:utf-8

import math as m

'''
算式 sqrt(n + 100) 与 sqrt(n + 268) 成立
=> n >= -100
'''
for i in range(-100, 10001):
    if m.sqrt(i+100) % 1 == 0 and m.sqrt(i+268) % 1 == 0:
        print(i)
    '''
    若没有导入 math，可以使用 ** 0.5
    if (i+100)**0.5 % 1 == 0 and (i+268)**0.5 % 1 == 0:
    '''

