#!/usr/bin/env python3
# coding:utf-8

def magic(num_lst):
    """对 num_lst 使用 1 次魔力"""
    n = len(num_lst)
    tmp = []
    for i in range(n-1):		# 又一种“移动”方法 “借替身”
        tmp.append(num_lst[i] + num_lst[i+1])
    tmp.append(num_lst[-1] + num_lst[0])
    for j in range(n):
        if tmp[j] >= 100:
            tmp[j] %= 100
    
    return tmp

if __name__ == '__main__':
    # 偷懒～
    # 假装 n = 5; k = 100; 传入数字为 1 2 3 4 5
    n, k = 5, 100
    num_lst = [1, 2, 3, 4, 5]
    
    for i in range(k):
        num_lst = magic(num_lst)     
    
    print(num_lst)

"""
magic() 中两个 for 循环可以叠加
for i in range(n-1):
    tmp.append((num_lst[i] + num_lst[i+1]) % 100)
tmp.append((num_lst[-1] + num_lst[0]) % 100)
"""