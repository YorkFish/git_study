#!/usr/bin/evn python3
# coding:utf-8

# 此法权当拓展思路
from math import sqrt

def is_prime(num):
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return "not"
    return num

prime_list = []
for i in range(100, 201):
    prime_list.append(is_prime(i))
while "not" in prime_list:
    prime_list.remove("not")
'''
上方两个循环可以这样改
for i in range(100, 201):
    tmp = is_prime(i)
    if tmp != 'not':
        prime_list.append(tmp)
但这样改完后，就相当于 008_05.py 了
'''

print(prime_list)
print("\nThere are {} prime numbers in total.".format(len(prime_list)))

