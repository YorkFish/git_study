#!/usr/bin/evn python3
# coding:utf-8

while True:
    try:
        n = int(input('请输入一个大于 1 的自然数:'))
        if n <= 1:
            print('输入有误，请重新输入')
            continue
        break
    except ValueError:
        print('输入有误，请重新输入')

prime_lst = [2]							# 配合下方的间隔 2，先把质数 2 存入
for i in range(3, n//2+3, 2):			# 存入足够多的质数；+3 是为了确保能进入循环；n//2+3 可以改成 int(n**0.5) + 1
    for j in range(2, int(i**0.5)+1):	# 判断质数
        if i % j == 0:
            break
    else:
        prime_lst.append(i)

idx = 0
print(n, "=", end=' ')
while n not in prime_lst:				# 只要 n 还是合数，就会进入这个循环
    if n % prime_lst[idx] == 0:
        n //= prime_lst[idx]
        print(prime_lst[idx], end=' x ')
    else:
        idx += 1
print(n)								# 此时的 n 是输入的数字分解后最大的一个质因数

