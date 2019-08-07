#!/usr/bin/evn python3
# coding:utf-8

from math import sqrt

prime_lst = []
for i in range(100, 201):
    tmp = int(sqrt(i)) + 1		# 与 tmp = int(sqrt(i) + 1) 效果相同
    for j in range(2, tmp):
        if i % j == 0:
            flag = 0
            break
    else:
        prime_lst.append(i)

print(prime_lst)
print("\nThere are {} prime numbers in total.".format(len(prime_lst)))

