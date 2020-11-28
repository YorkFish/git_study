#!/usr/bin/env python3
# coding:utf-8

def num_sum(n):
    """根据输入的 n 的奇偶性进行不同的加法，n<=0 情况下一律返回 0"""
    num = 0
    for i in range((n+1)%2+1, n+1, 2):	# 奇数 1 开头；偶数 2 开头
        num += 1/i
    
    return num

def run():
    n = int(input("Please enter a number: "))
    print("\nSum =", num_sum(n))

if __name__ == '__main__':
    run()

