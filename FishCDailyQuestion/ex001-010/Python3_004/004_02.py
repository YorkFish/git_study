#!/usr/bin/env python3
# coding:utf-8

year_input, month_input, day_input = [ int(x) for x in input("Please enter year/month/day(e.g. 2019/1/1): ").split('/')]
days_lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]		# 平年列表

def is_leap_year(year):										# 判断闰年与否
    return True if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else False

days_sum = sum( days_lst[ :month_input-1]) + day_input
if is_leap_year(year_input) and month_input > 2:
    days_sum += 1
print("\nCalculation results:", days_sum)

