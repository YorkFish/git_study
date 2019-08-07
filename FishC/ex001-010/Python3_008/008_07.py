#!/usr/bin/evn python3
# coding:utf-8

# “反证法”
from math import sqrt

total_lst = [ i for i in range(100, 201)]			# 存放 100 ~ 200
not_prime_lst = []									# 存入

for i in range(100, 201):
    for j in range(2, int(sqrt(i))+1):
        if i % j == 0:
            not_prime_lst.append(i)
            break

prime_set = set(total_lst) - set(not_prime_lst)		# 将两个列表转为集合，再取差集
print(sorted(prime_set))							# 给集合中的素数排序
print("\nThere are {} prime numbers in total.".format(len(prime_set)))

