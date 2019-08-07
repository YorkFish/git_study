#!/usr/bin/env python3
# coding:utf-8

# 桃子数累加；分桃顺着分
for peaches in range(6, 5000, 5):
    """
    6:    第 5 只猴子分之前至少有 6 只桃子
    5000: 答案不唯一，暂且在 5000 以内搜索
	5:    5 只猴子，每只每次 +1，故每次总共 +5
    """
    tmp = peaches
    for monkey in range(5):
        tmp = (tmp - 1) * 0.8	# *0.8 <---> /5 *4
        if tmp % 1 != 0:
            break
    else:
        print("Sum =", peaches)
        break

