#!/usr/bin/env python3
# coding:utf-8

# “直角三角形”输出
str_9x9 = ""					# 用字符串存放
for i in range(1, 10):			# i 控制行
    for j in range(1, i+1):		# j 控制列
        str_9x9 += "%d x %d = %2d  " % (j, i, i*j) if i!=j else "%d x %d = %2d  \n" % (j, i, i*j)

print(str_9x9)

