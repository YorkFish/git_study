#!/usr/bin/evn python3
# coding:utf-8

# “反证法”
from math import sqrt

not_prime = set()				# 存放非素数
for i in range(100, 201):
    for j in range(2, int(sqrt(i))+1):
        if i % j == 0:
            not_prime.add(i)    # 集合的内置函数中没有 append()
            break

for i in range(100, 201):
    if i not in not_prime:
        print(i, end=' ')
print("\n\nThere are {} prime numbers in total.".format(101-len(not_prime)))

