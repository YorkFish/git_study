#!/usr/bin/env python3
# coding:utf-8

# 将 006_06.py 的 for 版本改为 while 版本
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield a
        a, b = b, a + b
        n = n + 1

n = int(input("Please enter a number: "))
print("\nNo.{0} Fibonacci number is:".format(n), end=' ')
for i in fib(n):		# 改了一下输出方式
    pass
print(i)

