#!/usr/bin/env python3
# coding:utf-8

def get_num(num_lst):
    """一个列表搞定"""
    n = len(num_lst)
    i, k, m = 0, 0, 0
    while m < n-1:				# m = n-1 时退出循环
        if num_lst[i] != 0:		# i 是 num_lst 的标记
            k += 1				# k 是满 3 个数的标记
        if k == 3:
            num_lst[i] = 0		# 给退出者作标记
            k = 0
            m += 1
        i += 1
        if i == n:
            i = 0				# 进入下一轮循环
    
    idx = 0	
    while num_lst[idx] == 0:
        idx += 1
    print("\nThe lucky number is:", num_lst[idx])
'''
18 ~ 21 行的另一种写法
for i in range(n):
    if num_lst[i] != 0:
        print("\nThe lucky number is:", num_lst[i])
    break
'''

def run():
    n = int(input("Please enter the number of people: "))
    
    num_lst = []
    for i in range(n):
        num_lst.append(i+1)
    
    get_num(num_lst)
'''
run() 中的 num_lst 另一种写法 1
num_lst = [ (i+1) for i in range(int(input("...")))]

run() 中的 num_lst 另一种写法 2
num_lst = list( range(1, int(input("..."))+1))
'''

if __name__ == '__main__':
    run()

