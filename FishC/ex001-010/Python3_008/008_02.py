#!/usr/bin/evn python3
# coding:utf-8

from math import sqrt

prime_lst = []
for i in range(100, 201):
    tmp = int(sqrt(i))
    for j in range(2, tmp+1):	# 方便下方判断 j 与 tmp
        if i % j == 0:
            break
        elif j == tmp:
            prime_lst.append(i)

print(prime_lst)
print("\nThere are {} prime numbers in total.".format(len(prime_lst)))

