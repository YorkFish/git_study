#!/usr/bin/env python3
# coding:utf-8

from random import randint

num_lst = [ randint(1, 100) for _ in range(10)]
print("The original orandomer:", num_lst)

num_max = max(num_lst)
num_min = min(num_lst)

if num_lst[0] == num_max and num_lst[-1] == num_min:
    pass
else:
    if num_lst[0] != num_max:
        num_lst[num_lst.index(num_max)], num_lst[0] = num_lst[0], num_lst[num_lst.index(num_max)]	# 对 012_01.py 的改进
    if num_lst[-1] != num_min:
        num_lst[-1], num_lst[num_lst.index(num_min)] = num_lst[num_lst.index(num_min)], num_lst[-1]

print("\nAfter sorting:", num_lst)

