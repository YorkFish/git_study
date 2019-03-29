#!/usr/bin/evn python3
# coding:utf-8

# 输入数据并检查数据的合法性
num_input = input("Please enter a natural number greater than 1: ")
while not num_input.isdigit() or eval(num_input) < 2:
    num_input = input("Please enter a positive integer greater than 1 again: ")

num = int(num_input)					# “替身术”
prime_lst = []							# 存放质因数

# 记下方的 for 循环为 (*)
for i in range(2, int(num_input)+1):	# 此处可用 num + 1 代替 int(num_input) + 1
    while num % i == 0:
        num = num // i					# 统一数据类型为 int；这里不统一也能成功
        prime_lst.append(str(i))		# 方便使用 join()

print(num_input, "=", " x ".join(prime_lst))

'''
(*) 可以换成下方的语句
while num != 1:
    for i in range(2, num+1):
        if num % i == 0:
            prime_lst.append(str(i))
            num //= i
            break
'''

'''
(*) 可以换成下方的语句
for i in range(2, num//2+3):
    # num // 2 是为了减少运算
	# num//2 + 3 是防止 num = 2 或 num = 3 时进不了循环
	# num//2+3 可以改成 int(num**0.5) + 3
    if num >= i:
        while num % i == 0:
            prime_lst.append(str(i))
            num //= i
	# 可以加句 elif num == 1: break
'''

'''
(*) 可以换成下方的语句
k = 2
while k:		# 比较符合题目的分析
    if k == num:
        prime_lst.append(str(k))
        break
    elif k < num and num%k == 0:
        prime_lst.append(str(k))
        num //= k
    else:
        k += 1
'''

