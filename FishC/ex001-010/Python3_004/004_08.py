#!/usr/bin/env python3
# coding:utf-8

# 此代码相对健壮一点
year_input = input("please enter the year:  ")
while year_input.isdigit() != True or int(year_input) < 0:			# 判断输入的年份是否符合要求
    year_input = input("ERROR! Please enter the year again: ")
year = int(year_input)
if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    days_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]	# 闰年列表
else:
    days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]	# 平年列表

month_input = int(input("please enter the month: "))
months_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
while month_input not in months_list:								# 判断输入的月份是否符合要求
    month_input = int(input("ERROR! please enter the month again: "))

day_num = []
for i in range(days_list[month_input-1]):							# 现场填充一个月天数列表
    day_num.append(i+1)

day_input = int(input("please enter the day:   "))
while day_input not in day_num:										# 判断输入的日是否符合要求
    day_input = int(input("ERROR! please enter the day again: "))

days_sum = 0														# 总天数
while month_input > 1:												# 得到不计当月天数的总天数
    days_sum += days_list[month_input-2]
    month_input -= 1
days_sum += day_input												# 最后加上当月天数
print("\nCalculation results:", days_sum)

