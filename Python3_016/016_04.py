#!/usr/bin/env python3
# coding:utf-8

# 倒推
r = 0				# 初始化
peaches = 1			# 初始化
while peaches % 4:
    r += 4			# 5 只猴子分完桃，剩余桃子必是 4 的倍数
    peaches = r
    for monkey in range(4):
        peaches = peaches /4 *5 +1

print("Sum =", int(peaches /4 *5 +1))

