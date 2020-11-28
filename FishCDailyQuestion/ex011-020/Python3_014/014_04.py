#!/usr/bin/env python3
# coding:utf-8

def get_num(num_lst):
    n = 2 % len(num_lst)				# 防止 num_lst 因只有 2 个数而越界
    while len(num_lst) > 1:
        num_lst.pop(n)
        n = (n + 2) % len(num_lst)		# 每次都有隐身的 0 号位，所以只加 2；取余是为了循环
    
    print("\nThe lucky number is:", num_lst[0])
'''
get_num(num_lst) 的另一种写法 1，len(num_lst) >=3 时才奏效
n = 2
while len(num_lst) > 1:
    num_lst.pop(n)
    n += 2
    while len(num_lst) <= n:
        n -= len(num_lst)

get_num(num_lst) 的另一种写法 2，len(num_lst) >=3 时才奏效
n = 2
while len(num_lst) > 1:
    num_lst.pop(n)
    n += 2
    if len(num_lst) <= n:
        n %= len(num_lst)
'''

def run():
    num = int(input("Please enter the number of people: "))
    num_lst = list( range(1, num+1))
    get_num(num_lst)

if __name__ == '__main__':
    run()

