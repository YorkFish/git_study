#!/usr/bin/env python3
# coding:utf-8

from datetime import datetime

def days_calc(date):
    '''
    %Y 年份 0001~9999
    %m 月份 01~12
    %d 日期 01~31
    '''
    year  = date[:4] + '0101'
    start = datetime.strptime(year, '%Y%m%d')			# 当年第 1 天
    stop  = datetime.strptime(date, '%Y%m%d')			# 当天

    return (stop - start).days + 1						# 两个时间相减，再加上被减去的第 1 天

date_input = input("input date(e.g. 20190101): ")		# 其实 201911 也表示 19 年 1 月 1 日
print("\nCalculation results:", days_calc(date_input))

