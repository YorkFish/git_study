#!/usr/bin/evn python3
# coding:utf-8

# 对 009_08.py 做了改进
def prime_factors(n):
    '''Generate all prime factors of n.'''
    k = 2
    while k * k <= n:
        while not n % k:
            yield str(k)							# 改了此处
            n //= k
        k += 1
    if n > 1:
        yield str(n)								# 改了此处

# 输入数据并检查数据的合法性
num_input = input("Please enter a natural number greater than 1: ")
while not num_input.isdigit() or eval(num_input) < 2:
    num_input = input("Please enter a positive integer greater than 1 again: ")

prime_lst = list( prime_factors(int(num_input)))	# 用 list 提取 yield 中的数据；可回顾 006_06.py 和 006_07.py
print(num_input, "=", " x ".join(prime_lst))

