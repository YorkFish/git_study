#!/usr/bin/env python3
# coding:utf-8

# “直角三角形”输出
# 此程序像是 007_01.py 与 007_03.py 的杂糅版
str_9x9 = ""
for i in range(1, 10):			# i 控制行
    for j in range(1, i+1):		# j 控制列
        str_9x9 += "%d x %d = %2d  " % (j, i, i*j)
    str_9x9 += '\n'

print(str_9x9)

