#!/usr/bin/env python3
# coding:utf-8

# 倒推
a, b, c, d, e = 0.1, 0.1, 0.1, 0.1, 0	# a, b, c, d 初始值不能为 0，不然进不了 while 循环
while True:
    if d%1==0 and c%1==0 and b%1==0 and a%1==0:
        print("Sum =", int(5*a+1))
        break
    else:
        '''
        不妨设轮到“猴子乙”分桃，分之前有 q 个桃子，分之后剩 h 个桃子
        q 必是 4 的倍数
            因为上一只猴子留下的是 5 份中的 4 份
        不妨记 q = 4n，则 (4n -1) 必是 5 的倍数
            因为这一只猴子丢掉 1 个桃子后，剩余的能平均分 5 份
        不妨记 (4n - 1) = 5m，则 h = 4m
        (4n - 1) = 5m
        => n = (5m + 1) / 4				# n: 上一只猴子拿走的桃子数；m: 这一只猴子拿走的桃子数
        '''
        e += 1							# 第 5 只猴子拿走的桃子数；e += 5也行，但是是巧合
        d = (5 * e + 1) / 4				# 第 4 只猴子拿走的桃子数
        c = (5 * d + 1) / 4				# 第 3 只猴子拿走的桃子数
        b = (5 * c + 1) / 4				# 第 2 只猴子拿走的桃子数
        a = (5 * b + 1) / 4				# 第 1 只猴子拿走的桃子数
