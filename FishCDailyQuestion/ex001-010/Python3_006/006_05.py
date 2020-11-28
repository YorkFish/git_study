#!/usr/bin/env python3
# coding:utf-8

def fib(n, f=0, s=1):	# 递归
    '''
	n：第 n 个数
	f：前一个值
	s：后一个值
	'''
    if n == 1:
        return f
    else:
        return fib(n-1, s, f+s)

n = int(input("Please enter a number: "))
print("\nNo.{0} Fibonacci number is {1}.".format(n, fib(n)))

