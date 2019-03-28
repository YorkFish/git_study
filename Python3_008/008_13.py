#!/usr/bin/env python3
# coding:utf-8

# 此法权当拓展思路
from math import sqrt

num_count, col_count = 0, 0
for i in range(101, 201):
    flag = True
    for j in range(2, int(sqrt(i))+1):
        if i % j == 0:
            flag = False
            break
    if flag:
        print("{}".format(i), end=' ')
        num_count += 1				# 记录素数个数
        col_count += 1
        if col_count % 10 == 0:		# 10 个一行，排队
            col_count = 0
            print()

print("\n\nThere are {} prime numbers in total.".format(num_count))

