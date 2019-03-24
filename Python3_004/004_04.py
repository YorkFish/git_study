#!/usr/bin/env python3
# coding:utf-8

def days_calc(year, month, day):
    days_sum = 0							# 总天数
    Feb = 29 if (year%4 == 0 and year%100 != 0) or year%400 == 0 else 28
    for i in range(1, month):				# 得到不计当月天数的总天数
        if i in [1, 3, 5, 7, 8, 10, 12]:	# 31 天组
            days_sum += 31
        elif i == 2:						# 2 月
            days_sum += Feb
        else:								# 30 天组
            days_sum += 30

    return days_sum + day					# 最后加上当月天数

year_input, month_input, day_input = [ int(x) for x in input("Please enter year/month/day(e.g. 2019/1/1): ").split('/')]
print("\nCalculation results:", days_calc(year_input, month_input, day_input))

