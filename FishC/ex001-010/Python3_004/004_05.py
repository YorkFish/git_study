#!/usr/bin/env python3
# coding:utf-8

year_input, month_input, day_input = [ int(x) for x in input("Please enter year/month/day(e.g. 2019/1/1): ").split('/')]
days_lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]	# 平年列表

if (year_input%4 == 0 and year_input%100 != 0) or year_input%400 == 0:
    days_lst[1] = 29									# 若是闰年，将 2 月改为 29 天

days_sum = 0											# 总天数
for i in range(month_input-1):							# 得到不计当月天数的总天数
    days_sum = days_sum + days_lst[i]
days_sum += day_input									# 最后加上当月天数

print("\nCalculation results:", days_sum)

