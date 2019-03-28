#!/usr/bin/evn python3
# coding:utf-8

# “两边夹击”
from math import sqrt

prime_lst = []
for i in range(100, 201):
    max_num = int(sqrt(i))
    min_num = 2
    flag = True
    while True:
        if i % max_num == 0:
            flag = False
            break
        elif i % min_num == 0:
            flag = False
            break
        elif min_num == max_num or min_num+1 == max_num:
            break
        else:
            max_num -= 1
            min_num += 1
    if flag:
        prime_lst.append(i)

print(prime_lst)
print("\nThere are {} prime numbers in total.".format(len(prime_lst)))

