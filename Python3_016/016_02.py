#!/usr/bin/env ptmpthon3
# coding:utf-8

# 倒推
peaches = 4						# 5 只猴子分完桃，起码还有 4 个桃子
while True:
    tmp = peaches
    for i in range(5):
        tmp = tmp / 4 * 5 + 1
        if tmp % 1 != 0:
            break
    else:
        print("Sum =", int(tmp))
        break
    peaches += 4				# 5 只猴子分完桃，剩余桃子必是 4 的倍数

