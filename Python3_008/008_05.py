#!/usr/bin/evn python3
# coding:utf-8

from math import sqrt

def is_prime_num(num):
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False	# 非素数，返回 False
    return True				# 是素数，返回 True

count = 0
for i in range(100, 201):
    if is_prime_num(i):
        print(i, end=' ')
        count += 1
print("\n\nThere are {} prime numbers in total.".format(count))

