#!/usr/bin/evn python3
# coding:utf-8

from math import sqrt

# 类似 008_08.py
lst1 = list(range(100, 201))
lst2 = lst1[:]    # 对 lst2 操作将不影响 lst1

for i in lst1:
    for j in range(2, int(sqrt(i))+1):
        if i % j == 0:
            lst2.remove(i)
            break

print(lst2)
print("\nThere are {} prime numbers in total.".format(len(lst2)))

