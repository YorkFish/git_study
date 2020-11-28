#!/usr/bin/env python3
# coding:utf-8

# 这里的输入限制格式，也限制了年份，如 20,000 年
date = input("Please enter the date(e.g. 20190101): ")

year_input  = int(date[:4])				# 前 4 位数表示年份
month_input = int(date[4:6])			# 5、6 两位表示月份
day_input   = int(date[6:])				# 7、8 两位表示日
md_input    = int(date[4:])				# 最后 4 位表示月、日

days_lst = [0, 31, 28, 31, 30, 31, \
            30, 31, 31, 30, 31, 30, 31]	# 平年列表（前面多了个 0）
days_sum = 0							# 总天数

if (year_input%4 == 0 and year_input%100 != 0) or year_input%400 == 0:
    if md_input > 228:					# 判断输入的日子是否大于 2 月 28
        days_sum = 1
    else:
        days_sum = 0

for i in days_lst[:month_input]:		# 平年列表首位为 0，所以 month_input 不必减 1
    days_sum += i
days_sum += day_input

print("\nCalculation results:", days_sum)

