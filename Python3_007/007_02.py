#!/usr/bin/env python3
# coding:utf-8

# “直角三角形”输出
# 此程序是 007_01.py 的 while 版本
i = 1
while i <= 9:					# i 控制行
    for j in range(1, i+1):		# j 控制列
        print("%s x %s = %2s" % (j, i, i*j), end='  ')
    print()
    i += 1

