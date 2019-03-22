#!/usr/bin/env python3
# coding:utf-8

arr = [1000000, 600000, 400000, 200000, 100000, 0]		# 利润界限
rat = [0.01,    0.015,  0.03,   0.05,   0.075,  0.1]	# 每档利润对应的提成比率

def bonus_calc(profit):
    """根据利润计算奖金"""
    bonus = 0
    for i in range(len(arr)):
        if profit > arr[i]:
            bonus += (profit - arr[i]) * rat[i]			# 大于临界值的部分
            
            for j in range(i, len(arr)-1):				# 小于临界值的部分是固定的
                bonus += (arr[j] - arr[j+1]) * rat[j+1]

            return bonus
    else:
	    print("没有利润，要什么自行车！")				# 利润 <=0 的情况

    return None

profit_input = int(input("Please enter current month profit: "))
print("\nbonus = {}".format(bonus_calc(profit_input)))

