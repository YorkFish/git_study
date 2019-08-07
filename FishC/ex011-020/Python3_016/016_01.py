#!/usr/bin/env python3
# coding:utf-8

# 倒推
peaches = 4							# 第 5 只猴子分完桃，起码剩 4 个桃子
while peaches < 5000:				# 答案不唯一，暂且在 5000 以内搜索
    tmp = peaches
    for i in range(5):				# 5 只猴子
        tmp = tmp / 4 * 5 + 1		# 从第 5 只猴子倒推至第 1 只
    if tmp % 1 == 0:
        print("Sum = %d" % tmp)
        break
    else:
        peaches += 4				# 5 只猴子分完桃，剩余桃子必是 4 的倍数

