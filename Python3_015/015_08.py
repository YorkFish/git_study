#!/usr/bin/env python3
# coding:utf-8

# 此法虽“画蛇添足”，但不失为一条思路
def plus(n, s):					# 加法
    s += 1 / n
    n -= 2
    
    return (n, s)

def even(n):					# 输入偶数时所需调用的函数
    sum = 0
    while n >= 2:
        sum = plus(n, sum)[1]	# 知识点
        n = plus(n, sum)[0]
    
    return sum

def odd(n):						# 输入奇数时所需调用的函数
    sum = 0
    while n >= 1:
        sum = plus(n, sum)[1]
        n = plus(n, sum)[0]
    
    return sum

def run():
    num = int(input("Please enter a number: "))
    
    if num % 2 == 0:			# 为偶数时的结果
        print(even(num))
    else:						# 为奇数时的结果
        print(odd(num))

if __name__ == '__main__':
    run()

