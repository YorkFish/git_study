#!/usr/bin/env python3
# coding:utf-8

# “直角三角形”输出
# 此程序是对 007_07.py 的改进
from itertools import product

s = product(range(1,10), repeat=2)

for i in s:
    if i[0] > i[1]:		# 行数大于列数，水平输出，添加空格
        print("%s x %s = %2s" % (i[1], i[0], i[0] * i[1]), end='  ')
    elif i[0] == i[1]:	# 行数等于列数，输出后回车
        print("%s x %s = %2s" % (i[1], i[0], i[0] * i[1]))
        continue

