#!/usr/bin/env python3
# coding:utf-8

def bonus_calc(profit):
    lst = [ [1e6, 0.01], \
            [6e5, 0.015], \
            [4e5, 0.03], \
            [2e5, 0.05], \
            [1e5, 0.075], \
            [0,   0.1]]					# 倒序建立区间 [利润临界值 a, a 到下一个临界值之间的提成率]
    bonus = 0							# 奖金

    for i,j in lst:						# 遍历
        if i < profit:					# 得到小于 profit 的键
            bonus += (profit - i) * j	# 累加 (key * value)
            profit = i

    return bonus

profit_input = int(input("Please enter current month profit: "))
print("\nbonus = {}".format(bonus_calc(profit_input)))

