#!/usr/bin/env python3
# coding:utf-8

import numpy as np

def magic(num_lst, k):
    """对 num_lst 使用 k 次魔力"""
    for i in range(k):
        lst = np.append(num_lst[1:], num_lst[0])	# 将第一个元素放到最后，相当于数组循环左移一格
        num_lst = (num_lst + lst) % 100				# 模 100，不影响小于 100 的值
    
    return num_lst

if __name__ == '__main__':
    # 偷懒～
    # 假装 n = 5; k = 100; 传入数字为 1 2 3 4 5
    n, k = 5, 100
    num_lst = [1, 2, 3, 4, 5]
    
    print(magic(num_lst, k))

