#!/usr/bin/evn python3
# coding:utf-8

# 改进了 009_03.py 列表使用方面的不足；使用了埃拉托色尼的“筛选法”
def collect_prime(n, lst=[]):
    primes = [True] * int(n**0.5 + 1)							# 判断质数最多需要检查 sqrt(n) 次
    primes[0], primes[1] = False, False							# 0 和 1 不用

    for i, prime in enumerate(primes):							# 枚举
        if prime:
            for j in range(i*i, int(n**0.5+1), i):				# 用“埃拉托色尼筛选法”筛掉了一部分合数
                primes[j] = False

    prime_lst = [ k for k,prime in enumerate(primes) if prime]	# 取出 primes 中 True 的下标
    for p in prime_lst:
        if n % p == 0:
            return collect_prime(n//p, lst+[str(p)])			# 用 + 代替 append()
    return lst + [str(n)]

num_input = input("Please enter a natural number greater than 1: ")
while not num_input.isdigit() or eval(num_input) < 2:
    num_input = input("Please enter a positive integer greater than 1 again: ")

prime_lst = collect_prime(int(num_input))
print(num_input, "=", " x ".join(prime_lst))

