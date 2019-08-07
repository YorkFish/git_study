#!/usr/bin/env python3
# coding:utf-8

n = int(input("Please enter a number: "))

fib_lst = [0, 1]
if n > 2:
    for i in range(n-2):							# 因为前两个数已给出，所以超过几个，循环几次
        fib_lst.append(fib_lst[-1] + fib_lst[-2])	# 这个逻辑比较接近题目

print("\nNo.{0} Fibonacci number is {1}.".format(n, fib_lst[n-1]))

