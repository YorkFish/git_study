#!/usr/bin/env python3
# coding:utf-8

days_dict = {'common_year': [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],\
             'leap_year':   [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]}

judge = lambda y: 'leap_year' if (y%4 == 0 and y%100 != 0 or y%400 == 0) else 'common_year'

try:
    year_input  = int(input("year:  "))		 					# 输入所要计算的年份  
    month_input = int(input("month: "))							# 输入所要计算的月份
    day_input   = int(input("day:   "))							# 输入所要计算的日
    days_list   = days_dict[judge(year_input)]					# 判断是否闰年并得到相应的月天数列表

    # 检查输入的年、月、日的合法性
    if year_input >= 0 and 0 < month_input <= 12 and 0 < day_input <= days_list[month_input-1]:
        days_sum = sum(days_list[:month_input-1])+ day_input	# 不计当月天数的总天数 + 当月天数
        print("\nCalculation results:", days_sum)
    else:
        print("The input is beyond the reasonable range. Please re-enter it.")
        
except ValueError:
    print("Input format is incorrect.")

