#!/usr/bin/env python3
# coding:utf-8

from fractions import Fraction		# 可以算分数

def num_sum(n):
    return sum([ Fraction(1, i) for i in range(n, 0, -2)])

def run():
    n = int(input("Please enter the number: "))
    print("\nSum =", num_sum(n))

if __name__ == '__main__':
    run()

