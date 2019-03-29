#!/usr/bin/evn python3
# coding:utf-8

# 对 009_05.py 的改进
def de_factor(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print("%d x" % i, end=' ')
            return de_factor(n//i)
    print(n)

num_input = input("Please enter a natural number greater than 1: ")
while not num_input.isdigit() or eval(num_input) < 2:
    num_input = input("Please enter a positive integer greater than 1 again: ")

print(num_input, end=" = ")
de_factor(int(num_input))

