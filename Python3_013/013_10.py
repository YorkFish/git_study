#!/usr/bin/env python3
# coding:utf-8

from random import choices
from functools import reduce

def calc(x, y):
    _sum = x + y					# _sum 为保护变量
    if _sum >= 100:
        _sum %= 100
    tmp.append(_sum)

    return y

if __name__ == '__main__':
    # 偷懒用，随机选 50 个数字
    num_lst = choices([ x for x in range(1,101)], k=50)
    
    for x in range(200):			# 使用“魔力”的次数
        tmp = []
        num_lst.append(num_lst[0])
        reduce(calc, num_lst)		# (*)
        num_lst = tmp
    
    print(num_lst)

'''
(*) 可以这样理解
t = calc(num_lst[0], num_lst[1])	# 于此同时，tmp 中加入了两数之和
t = calc(t, num_lst[2])
t = calc(t, num_lst[3])
t = calc(t, num_lst[4])
t = calc(t, num_lst[5])
'''

