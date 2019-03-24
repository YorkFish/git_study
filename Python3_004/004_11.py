#!/usr/bin/env python3
# coding:utf-8

from datetime import datetime		# datetime 可以直接计算两个日期间的差

year_input, month_input, day_input = [ int(x) for x in input("input year/month/day(e.g. 2019/1/1): ").split('/')]
print((datetime(year_input, month_input, day_input) - datetime(year_input-1, 12, 31)).days)

