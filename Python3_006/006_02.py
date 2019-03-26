#!/usr/bin/env python3
# coding:utf-8

# 把 006_01.py 的语句“装”到函数里
def fib(max): 
    a, b = 0, 1 
    for i in range(max-1): 
        a, b = b, a + b
    
    return a

'''
把上方的语句换成 while 形式
def fib(max): 
    n, a, b = 1, 0, 1 
    while n < max: 
        a, b = b, a + b
        n += 1
    
    return a
'''

n = int(input("Please enter a number: "))
print("\nNo.{0} Fibonacci number is {1}.".format(n, fib(n)))

