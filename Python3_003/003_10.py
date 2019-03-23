#!/usr/bin/env python3
# coding:utf-8

# 此法权当拓展思路
from math import sqrt

for i in range(-100, 10001):
    '''
    一般地
	sqrt(10) = 3.1622776601683795
	len(str(sqrt(10))) = 18

    sqrt(100) = 10.0
    len(str(sqrt(100))) = 4

    但是，会丢根
    sqrt(10000) = 100.0, len(str(str(sqrt(10000)))) = 5
	sqrt(9) = 3.0, len(str(sqrt(9))) = 3
	即对于小于等于 (10000 + 268) 的完全平方数 n，len(str(sqrt(n))) 的结果可能是 3，4，5
	遇到 3 对 4，或者 4 对 5 的情况时，会错过答案
    '''
    str1 = str(sqrt(i + 100))
    str2 = str(sqrt(i + 268))
    if len(str1) == len(str2) == 4:
        print(i)

