#!/usr/bin/env python3
# coding:utf-8

# 桃子数累加；分桃顺着分
tale = 6				# s 表示桃子总数
peaches = 6				# “替身”
monkeys = 5				# 分 5 次
while monkeys:
    if (peaches - 1) % 5 != 0:
        tale += 5
        peaches = tale
        monkeys = 5		# 重置
    else:
        monkeys -= 1
        peaches = (peaches - 1) * 0.8

print("Sum =", tale)	# 答案不唯一

