#!/usr/bin/env python3
# coding:utf-8

from random import randint

num_lst = [ randint(1, 100) for _ in range(10)]							# 偷懒~ 让程序随机选 10 个数
print("The original order:", num_lst)

num_max = max(num_lst)
num_min = min(num_lst)

if num_lst[0] == num_max and num_lst[-1] == num_min:					# 运气好，天生满足要求
    pass
else:
    if num_lst[0] != num_max:
        max_idx = num_lst.index(num_max)								# (1)
        num_lst[0], num_lst[max_idx] = num_lst[max_idx], num_lst[0]		# (2)
    if num_lst[-1] != num_min:
        num_lst[-1], num_lst[num_lst.index(num_min)] = num_lst[num_lst.index(num_min)], num_lst[-1]

print("\nAfter sorting:", num_lst)

'''
(1) 与 (2) 不能合成 num_lst[0], num_lst[num_lst.index(num_max)] = num_lst[num_lst.index(num_max)], num_lst[0]
012_02.py 有解决方法
'''

