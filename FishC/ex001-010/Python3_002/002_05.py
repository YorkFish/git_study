#!/usr/bin/env python3
# coding:utf-8

list1 = [1000000, 600000, 400000, 200000, 100000, 0]		# 利润界限 a form [a, b, c, ...] 
list2 = [0.01,    0.015,  0.03,   0.05,   0.075,  0.1]		# 超过 a 的提成率
list3 = [39500,   33500,  27500,  17500,  10000,  0]		# 利润界限 a 以内最大提成金额

profit = int(input("Please enter current month profit: "))

for i in range(len(list1)):
    if profit > list1[i]:
        break												# 感觉怪怪的，但确实存住了 i 的值

bonus = (profit - list1[i]) * list2[i] + list3[i]
print("\nbonus = {}".format(bonus))

