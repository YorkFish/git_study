#!/usr/bin/env python3
# coding:utf-8

'''
普通闰年：能被 4 整除，但不能被 100 整除的年份为普通闰年
    如 2004 年就是闰年，1999 年不是闰年

世纪闰年：能被 400 整除的年份为世纪闰年
    如 2000 年是世纪闰年，1900 年不是世纪闰年
'''

year_input  = eval(input("Please enter the year:  "))			# 输入所要计算的年份
month_input = eval(input("Please enter the month: "))			# 输入所要计算的月份
day_input   = eval(input("Please enter the date:  "))			# 输入所要计算的日

leap_lst   = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]	# 闰年列表
common_lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]	# 平年列表

def is_leap_year(year):											# 判断闰年与否
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:		# 不加括号也行，加上看着清楚
        return leap_lst											# 返回闰年列表
    else:
        return common_lst										# 返回平年列表

def days_calc(month, day, days_lst):
    days_sum = 0												# 总天数
    for i in range(month-1):
        days_sum += days_lst[i]
    days_sum += day

    return days_sum												# 返回总天数

days_list = is_leap_year(year_input)							# 得到 闰年/平年 列表
days = days_calc(month_input, day_input, days_list)				# 得到总天数
print("\nCalculation results:", days)

