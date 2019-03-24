#!/usr/bin/env python3
# coding:utf-8

year_input  = int(input("year:  "))				# 输入所要计算的年份
month_input = int(input("month: "))				# 输入所要计算的月份
day_input   = int(input("day:   "))				# 输入所要计算的日

days_lst = (0, 31, 59, 90, 120, 151, \
            181, 212, 243, 273, 304, 334)		# 已经算好的天数，放元组里比放列表中更好

if 0 < month_input <= 12:						# 检查输入的月份
    days_sum = days_lst[month_input - 1]		# 得到不计当月天数的总天数
else:
    print("Please enter the correct month!")	# 此处可进一步完善

days_sum += day_input
if (year_input%4 == 0 and year_input%100 != 0) or year_input % 400 == 0:
    if month_input > 2:
        days_sum += 1							# 是闰年，且是 3 月或 3 月以上，加一天

print("\nCalculation results:", days_sum)

