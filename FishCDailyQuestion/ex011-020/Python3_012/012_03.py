#!/usr/bin/env python3
# coding:utf-8

from random import randint

num_lst = [ randint(1, 100) for _ in range(10)]							# 偷懒~ 让程序随机选 10 个数
print("The original order:", num_lst)

# 算是对 012_01.py 的一种改进
max_idx = num_lst.index(max(num_lst))									# 取出最大值的索引值
min_idx = num_lst.index(min(num_lst))									# 取出最小值的索引值

if max_idx == 0 and min_idx == len(num_lst)-1:							# 运气好，天生满足要求
    pass
else:
    if max_idx != 0:
        num_lst[0], num_lst[max_idx] = num_lst[max_idx], num_lst[0]
    if min_idx != len(num_lst)-1:
        num_lst[-1], num_lst[min_idx] = num_lst[min_idx], num_lst[-1]

print("\nAfter sorting:", num_lst)

