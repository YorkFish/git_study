#!/usr/bin/evn python3
# coding:utf-8

def prime_factors(n):
    '''Generate all prime factors of n.'''
    k = 2
    while k * k <= n:
        while not n % k:
            yield str(k)+" x"	# 有待改进,见 009_09.py
            n //= k
        k += 1
    if n > 1:					# 最大的质因数
        yield n					# 这个数字可以不转换成字符

print(198, "=", end=' ')		# 偷懒,不手动输入数字了～
for i in prime_factors(198):	# 偷懒~
    print(i, end=' ')

