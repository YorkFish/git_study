#!/usr/bin/evn python3
# coding:utf-8

# 此法权当拓展思路
from math import sqrt

flag, count, raw = 1, 0, 0
for i in range(101, 200, 2):	# 偶数肯定不是素数
    for j in range(2, int(sqrt(i))+1):
        if i % j == 0:
            flag = 0
            break
    if flag:					# flag 不用 True 和 False，用 0 和 1 也行
        print("{:>3}".format(i), end=' ')
        count += 1				# 记录最后一行的素数的个数
        if count == 10:			# 10 个一组
            count = 0			# 清 0
            raw += 1			# 行数加 1
            print()
    else:
        flag = 1

print("\n\nThere are {} prime numbers in total.".format(raw*10+count))

