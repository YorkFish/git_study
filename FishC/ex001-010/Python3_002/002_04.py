#!/usr/bin/env python3
# coding:utf-8

# 形式：临界值:[下一档的提成率, 此临界值下总共能提成的金额]
bonus_dict = {100000:[0.075, 10000], \
              200000:[0.05,  17500], \
              400000:[0.03,  27500], \
              600000:[0.015, 33500], \
             1000000:[0.01,  39500]}

def bonus_calc(profit, bonus_dict=bonus_dict):
    """照理说，字典是无序的，但此函数依赖了 bonus_dict 的“顺序”，所以不推荐这种做法"""
    profit_list = [ i for i in bonus_dict.keys() if i < profit]

    if profit_list == []:					# 若要防止 profit <= 0，可以在输入时作判断；或将此 if 语句嵌入另一个 if 语句中
        return profit * 0.1
    else:
        temp = [ profit_list[-1]] + bonus_dict[ profit_list[-1]]
        return (profit - temp[0]) * temp[1] + temp[2]

profit_input = int(input("Please enter current month profit: "))
print("\nbonus = {}".format(bonus_calc(profit_input)))

