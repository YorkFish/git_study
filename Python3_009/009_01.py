#!/usr/bin/evn python3
# coding:utf-8

# 输入并检查合法性
num_input = input("Please enter a natural number greater than 1: ")
while not num_input.isdigit() or eval(num_input) < 2:
    num_input = input("Please enter a positive integer greater than 1 again: ")

num = int(num_input)				# “替身术”
k = 2								# 根据题意，存放每一轮的最小质数
prime_lst = []						# 存放质因数

while num > 1:						# 算完最后一个质数，num = 1
    if num % k == 0:
        prime_lst.append(str(k))	# 方便使用 join()
        num //= k
    else:
        k += 1						# 因为 k 是从 2 开始增长的，所以每当 k 为合数时，不会执行上方的 if 语句

print(num_input, "=", " x ".join(prime_lst))  

