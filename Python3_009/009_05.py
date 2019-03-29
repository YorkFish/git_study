#!/usr/bin/evn python3
# coding:utf-8

# 009_03.py 的另一种改进
def collect_prime(n):					# (*)
    global prime_lst					# 话说回来，这句不写也行
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            prime_lst.append(str(i))
            return collect_prime(n//i)
    prime_lst.append(str(n))			# 最后一个质因数
    
    return prime_lst

prime_lst = []

# 输入数据并检查数据的合法性
num_input = input("Please enter a natural number greater than 1: ")
while not num_input.isdigit() or eval(num_input) < 2:
    num_input = input("Please enter a positive integer greater than 1 again: ")

print(num_input, "=", " x ".join(collect_prime(int(num_input))))

'''
(*) 可以改成如下样子
def collect_prime(n):
    k = 2
    while n != 1:
        if n % k == 0:
            prime_lst.append(str(k))
            return collect_prime(n//k)
        k += 1

相应的输出要改为
collect_prime(int(num_input))
print(num_input, "=", " x ".join(prime_lst))
'''

