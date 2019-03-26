#!/usr/bin/env python3
# coding:utf-8

n = int(input("Please enter a number: "))

a, b = 0, 1
for i in range(n-1):		# 第一组数据是给出的，所以是 n-1 次循环
    a, b = b, a+b

print("\nNo.{0} Fibonacci number is {1}.".format(n, a))

