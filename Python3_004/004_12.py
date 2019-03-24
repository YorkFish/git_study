#!/usr/bin/env python3
# coding:utf-8

from datetime import date		# 和 004_11.py 换汤不换药，date(y1, m1, d1).__sub__(date(y2, m2, d2)) 计算两个日期之差

year_input, month_input, day_input = [ int(x) for x in input("input year/month/day(e.g. 2019/1/1): ").split('/')]
print(date(year_input, month_input, day_input).__sub__(date(year_input-1, 12, 31)).days)

