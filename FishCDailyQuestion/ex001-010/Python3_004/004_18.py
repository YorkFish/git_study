#!/usr/bin/env python3
# coding:utf-8

import calendar

def days_calc(date):
    year  = int(date[:4])
    month = int(date[4:6])
    day   = int(date[6:])
    days_sum = 0

    if month == 1:
        return day
    else:
        for i in range(1, month):					# 得到不计当月天数的总天数
            days_sum += calendar.monthrange(year, i)[1]

    return days_sum + day							# 最后加上当月天数

date_input = input("input date(e.g. 20190101): ")	# 不能写成 201911
print("\nCalculation results:", days_calc(date_input))

