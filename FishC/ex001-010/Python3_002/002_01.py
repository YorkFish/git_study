#!/usr/bin/env python3
# coding:utf-8

profit = int(input("Please enter current month profit: "))		# 输入当月利润

arr = [1000000, 600000, 400000, 200000, 100000, 0]				# 利润界限
rat = [0.01,    0.015,  0.03,   0.05,   0.075,  0.1]			# 提成率
bonus = 0														# 奖金

for idx in range(6):
    if profit > arr[idx]:
        bonus += (profit - arr[idx]) * rat[idx]
        profit = arr[idx]

print("\nbonus = {}".format(bonus))

