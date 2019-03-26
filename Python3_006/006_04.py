#!/usr/bin/env python3
# coding:utf-8

def fib(n):		# 递归
    if n <= 0:
        print("Input error！")
        return -1
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1      
    else:
        return fib(n-1) + fib(n-2)
    
n = int(input("Please enter a number: "))
result = fib(n)
if result != -1:
    print("\nNo.{0} Fibonacci number is {1}.".format(n, result))

