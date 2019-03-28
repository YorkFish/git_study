#!/usr/bin/evn python3
# coding:utf-8

from math import sqrt

prime_lst = []
for i in range(100, 201):
    flag = 1
    tmp = int(sqrt(i) + 1)	# 1 range() 中不能放 float；2 可以用 i**0.5 代替 sqrt(i) 开方
    for j in range(2, tmp):
        if i % j == 0:
            flag = 0
            break
    if flag:
        prime_lst.append(i)

print(prime_lst)
print("\nThere are {} prime numbers in total.".format(len(prime_lst)))

