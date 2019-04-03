#!/usr/bin/env python3
# coding:utf-8

def get_num(num_lst):
    i = 1							# num_lst 的标记
    m = 0							# num_lst 的下标
    while len(num_lst) > 1:
        if i == 3 and m < len(num_lst):
            num_lst.pop(m)
            i = 1
            continue
        elif m > len(num_lst) - 1:	# 下标值出界
            m = 0					# 为了循环
            continue
        i += 1
        m += 1
    
    print("\nThe lucky number is:", num_lst[0])

def run():
    n = int(input("Please enter the number of people: "))
    num_lst = list( range(1, n+1))
    get_num(num_lst)

if __name__ == '__main__':
    run()

