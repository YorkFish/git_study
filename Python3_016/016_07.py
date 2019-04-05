#!/usr/bin/env python3
# coding:utf-8

# 桃子数累加；分桃顺着分
peaches = 6						# 第 5 只猴子分之前至少有 6 只桃子
while 1:
    monkeys = 5					# 5 只猴子
    tmp = peaches
    while monkeys > 0:
        if (tmp - 1) % 5 == 0:
            tmp = (tmp - 1) /5 *4
            monkeys -= 1
        else:
        	break
    if monkeys == 0:
    	print("Sum =", peaches)
    	break
    else:
    	peaches += 5			# 5 只猴子，每只每次 +1，故每次总共 +5

