#!/usr/bin/env python3
# coding:utf-8

def is_leap_year(year):						# 判断闰年与否
    if(year%4 == 0 and year%100 != 0) or year%400 == 0:
        return True
    else:
        return False

months_list = [12, 11, 10,  9,  8,  7,  6,  5,  4,  3,  2,  1]
days_list   = [31, 30, 31, 30, 31, 31, 30, 31, 30, 30, 28, 31]

year_input  = int(input("year:  "))			# 输入所要计算的年份  
month_input = int(input("month: "))			# 输入所要计算的月份
day_input   = int(input("day:   "))			# 输入所要计算的日
days_sum  = 0								# 总天数

for i in range(12):
    if months_list[i] < month_input:
        days_sum += days_list[i]

if(is_leap_year(year_input)):
    print("\nCalculation results:", days_sum + day_input + 1)
else:
    print("\nCalculation results:", days_sum + day_input)

