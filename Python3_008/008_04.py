#!/usr/bin/evn python3
# coding:utf-8

from math import sqrt
from math import fmod			# 取余

prime_lst = []
for i in range(100, 201):
    for j in range(2, int(sqrt(i))+1):
        if fmod(i, j) == 0:		# fmod(i, j) 相当于 i % j
            break
    else:
        prime_lst.append(i)

print(prime_lst)
print("\nThere are {} prime numbers in total.".format(len(prime_lst)))

