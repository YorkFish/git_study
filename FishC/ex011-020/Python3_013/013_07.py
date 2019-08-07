#!/usr/bin/env python3
# coding:utf-8

def magic(num_lst, n, k):
    """对 num_lst 使用 k 次魔力"""
    a = num_lst[:]
    for j in range(k):
        b = a[1:]						# 又一种“移动”方法
        b.append(a[0])
        for i in range(n):
            a[i] = (a[i] + b[i]) % 100	# 无差别对 100 取余
    
    return a

if __name__ == '__main__':
    # 偷懒～
    # 假装 n = 5; k = 100; 传入数字为 1 2 3 4 5
    n, k = 5, 100
    num_lst = [1, 2, 3, 4, 5]
    
    print(magic(num_lst, n, k))

