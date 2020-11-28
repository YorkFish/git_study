#!/usr/bin/env python3
# coding:utf-8

from datetime import datetime

def days_calc(date):
    '''
    %Y 年份 0001~9999
    %m 月份 01~12
    %d 日期 01~31
    '''
    time1 = datetime.strptime(date, "%Y-%m-%d")
    temp = str(time1.year - 1) + "-12-31"
    time2 = datetime.strptime(temp, "%Y-%m-%d") 

    return time1 - time2									# 思路和 004_11.py 差不多

date = input("input year-month-day(e.g. 2019-01-01): ")		# 2019-1-1 也行
print("\nCalculation results:", days_calc(date))			# 结尾会多一个 0:00:00

