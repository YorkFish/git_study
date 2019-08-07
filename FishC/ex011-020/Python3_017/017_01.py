#!/usr/bin/env python3
# coding:utf-8

from random import randint

array = [ randint(-100, 100) for i in range(10)]
print("The initial array is:", array)

# 最小差值的初始化
diff_min = 200					# 可以用 abs(array[0] - array[1])；也可以往大了说一个

for i in range(9):				# 防止最后越界
    for j in range(i+1, 10):
        tmp = abs(array[i] - array[j])
        if diff_min > tmp:
            diff_min = tmp

print("\nMinimum difference is:", diff_min)

