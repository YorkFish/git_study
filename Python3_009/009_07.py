#!/usr/bin/evn python3
# coding:utf-8

# 对 009_04.py 的改进
def collect_prime(num, divisor=2, lst=[]):		# divisor 相当于题目分析中的 k
    if num%divisor == 0 and num != divisor:
        lst.append(str(divisor))
        return collect_prime(num/divisor, 2, lst)
    elif num % divisor != 0:
        return collect_prime(num , divisor+1, lst)
    elif num == divisor:						# 程序见底
        if len(lst) == 0:						# 输入的是质数
            return divisor
        lst.append(str(divisor))
        return " x ".join(lst)

num_input = input("Please enter a natural number greater than 1: ")
while not num_input.isdigit() or eval(num_input) < 2:
    num_input = input("Please enter a positive integer greater than 1 again: ")

print(num_input, "=", collect_prime(int(num_input)))

