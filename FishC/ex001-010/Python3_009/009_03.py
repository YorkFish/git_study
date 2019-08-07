#!/usr/bin/env python3
# coding:utf-8

# 此法权当拓展思路
from math import sqrt

#判断 n 是否为素数
def is_prime(n):
    if n <= 1:
        return 0
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return 0
    return 1

#利用递归分解 n 并打印质因数
prime_lst1 = []																# 此处有待改进，见后面的 009_04.py
def collect_prime(n):
    if is_prime(n):
        prime_lst1.append(str(n))											# 若 n 是质数，就不必做别的工作了；str() 是为了方便 join()
    else:
        k = 2
        # 若一个数 n 有质因数，则其必是合数，且 n >= 4
        # 因为 n 最小的质因数不会小于 2，所以其最大的质因数不会大于 n//2
        while k <= n//2:
            if n % k == 0:
                prime_lst1.append(str(k))									# 同上，方便使用 join()
                return collect_prime(n//k)									# 递归时，没有把 k 记录下来；若 n/k，数据变为 float，不统一
            k = k + 1
    
    return prime_lst1

num_input = int(input("Please enter a natural number greater than 1: "))	# 偷懒，不检查数据的合法性了～
prime_lst2 = collect_prime(num_input)
print(num_input, "=", " x ".join(prime_lst2))

