#!/usr/bin/env python3
# coding:utf-8

# 倒推
peaches = 4				# 5 只猴子分完桃，起码还有 4 个桃子
monkeys = 0
for i in range(1000):
    tmp = peaches
    for j in range(5):	# 5 只猴子，分桃 5 次
        if tmp % 4 == 0:
            monkeys += 1
        else:
            break
        tmp = tmp /4 *5 +1
    if monkeys == 5:
        print("Sum = %d" % tmp)
        break
    else:
        monkeys = 0
        peaches += 4	# 5 只猴子分完桃，剩余桃子必是 4 的倍数

