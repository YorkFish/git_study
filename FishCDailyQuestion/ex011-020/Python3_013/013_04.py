#!/usr/bin/env python3
# coding:utf-8

def magic(num_lst, k):
    """对 num_lst 使用 k 次魔力"""
    n = len(num_lst)
    num_lst.append(0)		# 又一种“移动”方法 "+1 -1"
    for i in range(k):
        num_lst[-1] = num_lst[0]
        for j in range(n):
            num_lst[j] += num_lst[j+1]
            if num_lst[j] >= 100:
                num_lst[j] %= 100
    num_lst.pop()			# 或 del num_lst[-1]

    return num_lst

if __name__ == '__main__':
    # 偷懒～
    # 假装 n = 5; k = 100; 传入数字为 1 2 3 4 5
    n, k = 5, 100
    num_lst = [1, 2, 3, 4, 5]

    print(magic(num_lst, k))

