#!/usr/bin/env python3
# coding:utf-8

'''
找规律
倒推可得数列 1，4，10，22，46...
数列的差值为 3，3*2，3*2*2，3*2*2*2...
'''
i = 1					# 第 10 天的桃子数
d = 3					# 倒推的第 1 个差值
for _ in range(9):		# 吃了九次
    i += d				# 加差值
    d *= 2				# 升级差值
print("There are {} peaches in all.".format(i))

