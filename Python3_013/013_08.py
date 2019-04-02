#!/usr/bin/env python3
# coding:utf-8

import time

def magic(lst, k):
    """对 lst 使用 k 次魔力"""
    for i in range(k):
        lst1 = lst[:]
        lst2 = lst[:]
        lst2.append(lst2.pop(0))												# 又一种“移动”方法
        lst = list( map( lambda x,y: (x+y)%100, lst1, lst2))
    
    return lst

if __name__ == '__main__':
    n, k = input("Please input n and k: ").split()
    n, k = int(n), int(k)
    
    print(f"{n} numbers, cycle {k} times")
    num_lst = [ int(i) for i in input(f"\nPlease input {n} numbers: ").split()]
    
    time_start = time.time()													# 开始计时
    print(magic(num_lst, k))
    time_stop = time.time()														# 结束计时
    print("\nIt takes {:.6}us altogether.".format((time_stop-time_start)*1e6))	# 计算运行时间

