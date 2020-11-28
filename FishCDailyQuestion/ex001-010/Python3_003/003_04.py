#!/usr/bin/env python3
# coding:utf-8

'''
84^2 - 83^2 = 167
85^2 - 84^2 = 169
268 - 100 = 168
=> 84^2 - 83^2 < 268 - 100 < 85^2 - 84^2
=> 上限为 84^2

算式 sqrt(n + 100) 与 sqrt(n + 268) 成立
=> n + 100 >= 0
=> 下限为 0
'''
lst = [ i**2 for i in range(84, -1, -1)]

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] - lst[j] == 168:
            print(lst[i] - 268)
        elif lst[i] - lst[j] > 168:		# 不做无谓的的计算
            break

