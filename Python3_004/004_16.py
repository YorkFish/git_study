#!/usr/bin/env python3
# coding:utf-8

import time

days_sum = 0
days_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 导入 time 库只是单纯地更改了获取日期的“姿势”
date = input("Please enter year-month-day(e.g. 2019-01-01): ")
temp = time.strptime(date, "%Y-%m-%d")
year, month, day = temp[0:3]

for i in range(month):
    days_sum += days_list[i]
days_sum += day
if (year%4 == 0 and year%100 != 0) or year%400 ==0:
    if month > 2:
        days_sum += 1

print("\nCalculation results:", days_sum)

