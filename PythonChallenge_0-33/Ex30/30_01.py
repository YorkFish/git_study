#!/usr/bin/env python3
# coding:utf-8

def prime_factorization(num):
    factor = []
    for i in range(3, int(num**0.5), 2):
        if num % i == 0:
            factor.append(i)
            factor.append(num // i)
    print(factor)


if __name__ == "__main__":
    prime_factorization(7367)
