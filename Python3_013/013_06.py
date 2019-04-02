#!/usr/bin/env python3
# coding:utf-8

def str_2_int(num_lst):
    lst = []
    for i in num_lst:
        lst.append(int(i))
    
    return lst

def magic(num_lst, n, k):
    """对 num_lst 使用 k 次魔力"""
    for i in range(k):
        first = num_lst[0]										# 感觉 first 比 tmp 好
        for j in range(n-1):									# 省得用 len()；但有漏洞，如输入的数不是 n 个
            num_lst[j] += num_lst[j + 1]
            if num_lst[j] >= 100:
                num_lst[j] %= 100
        num_lst[n-1] += first
        if num_lst[n-1] >= 100:
            num_lst[n-1] %= 100
    
    return num_lst

if __name__ == '__main__':
    n, k = input("Please enter n and k(e.g. 5 20): ").split()	# 又一种输入方式
    n, k = int(n), int(k)
    
    num_lst = input("Input the numbers of the rings: ").split()
    num_lst = str_2_int(num_lst)								# 拓展思路嘛~
    
    print(magic(num_lst, n, k))

