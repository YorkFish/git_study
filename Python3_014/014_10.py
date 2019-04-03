#!/usr/bin/env python3
# coding:utf-8

def get_num(n, num_lst):
    if n < 1:
        print("Please enter a natural number greater than 0.")
    
    while num_lst:									# 最多只能将“元素”缩小到 2 个
        if len(num_lst) >= 3:
            num_lst.pop(2)
            num_lst = num_lst[2:] + num_lst[:2]		# 实现循环
        elif len(num_lst) <= 2:
            break
    
    print("\nThe lucky number is:", num_lst[-1])	# 2 个元素必是后者胜

def run():
    n = int(input("Please enter the number of people: "))
    num_lst = [ i for i in range(1, n+1)]
    get_num(n, num_lst)

if __name__ == '__main__':
    run()

