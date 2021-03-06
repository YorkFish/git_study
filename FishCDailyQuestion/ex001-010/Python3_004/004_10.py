#!/usr/bin/env python3
# coding:utf-8

def is_leap_year(year):						# 判断闰年与否
    if(year%4 == 0 and year%100 != 0) or year%400 == 0:
        return True
    else:
        return False

# 把 004_09.py 改成字典形式
md_dict = {1:31, 2:28, 3:31, 4:30, 5:51, 6:30, 7:31, 8:81, 9:30, 10:31, 11:30, 12:31}

year_input  = int(input("year:  "))			# 输入所要计算的年份  
month_input = int(input("month: "))			# 输入所要计算的月份
day_input   = int(input("day:   "))			# 输入所要计算的日
days_sum  = 0								# 总天数

for k in md_dict:
    if k < month_input:
        days_sum += md_dict[k]

if(is_leap_year(year_input)):
    print("\nCalculation results:", days_sum + day_input + 1)
else:
    print("\nCalculation results:", days_sum + day_input)

