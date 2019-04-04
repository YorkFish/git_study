#!/usr/bin/env python3
# coding:utf-8

def num_sum(n):
    tale = 0
    start = 1 if n % 2 == 1 else 2		# 奇数 1，偶数 2
    for i in range(start, n+1, 2):
        tale += 1 / i
    
    return tale
'''
while 版本：
def num_sum(n):
    tale = 0
    while n > 0:
        tale += 1 / n
        n -= 2

    return tale
'''

def run():
    n = int(input("Please enter the number: "))
    print("\nSum = {:.6f}".format(num_sum(n)))

if __name__ == '__main__':
    run()

