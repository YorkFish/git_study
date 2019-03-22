#!/usr/bin/env python3
# coding:utf-8

profit = int(input("Please enter current month profit: "))

bonus = 0
gear1 = 100000 * 0.1						# 第 1 档，10w  以内最高奖金
gear2 = gear1 + ( 200000-100000) * 0.075	# 第 2 档，20w  以内最高奖金
gear3 = gear2 + ( 400000-200000) * 0.05		# 第 3 档，40w  以内最高奖金
gear4 = gear3 + ( 600000-400000) * 0.03		# 第 4 档，60w  以内最高奖金
gear5 = gear4 + (1000000-600000) * 0.015	# 第 5 档，100w 以内最高奖金

if profit > 1000000:
    bonus += gear5 + (profit-1000000) * 0.01
elif profit > 600000:
    bonus += gear4 + (profit- 600000) * 0.015
elif profit > 400000:
    bonus += gear3 + (profit- 400000) * 0.03
elif profit > 200000:
    bonus += gear2 + (profit- 200000) * 0.05
elif profit > 100000:
    bonus += gear1 + (profit- 100000) * 0.075
elif profit > 0:
    bonus += (profit-100000) * 0.1
else:
    print("Input error, please input again.")

print("\nbonus = {}".format(bonus))

