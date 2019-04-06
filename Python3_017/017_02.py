#!/usr/bin/env python3
# coding:utf-8

from random import sample

array = sample( range(-100, 100), 10)				# 取 10 个不同重复的随机数
print("The initial array is:", array)

tmp_array = []
for i in range(9):									# 防止最后越界
    for j in range(i+1, 10):
        tmp_array.append(abs(array[i] - array[j]))	# 或者用 math.fabs(n1-n2) 求绝对值

print("\nMinimum difference is:", min(tmp_array))

