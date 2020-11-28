#!/usr/bin/env python3
# coding:utf-8

def num_sum(n):		# 递归
    if n == 1:
        return 1
    elif n == 2:
        return 1/2
    else:
        return num_sum(n-2) + 1/n

def run():
    n = int(input("Please enter a number: "))
    print("\nSum =", num_sum(n))

if __name__ == '__main__':
    run()

