#!/usr/bin/env python3
# coding:utf-8

'''
以 x^2 为中心，向左 -100，向右 +168
(x^2-100)  <-  -100  <-  (x^2)  ->  +168  ->  (y^2)

x 对应 sqrt(n + 100)
=> x >= 0
=> x 的下限为 0

x^2 -100 <= 10000
=> x < 100.5
又 x 为整数
=> x 的上限为 100

其实，借鉴 004_04.py 可知 x 的上限为 83
'''
print([ x*x-100 for x in range(84) if (x*x+168)**0.5 % 1 == 0])

