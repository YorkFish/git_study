#!/usr/bin/env python3
# coding:utf-8

import time

date = input("input date(e.g. 2019-01-01): ")	# 这里的 y-m-d 格式与 strptime 时的格式相同即可
days = time.strptime(date, "%Y-%m-%d")			# strptime 将时间转时间戳
print("\nCalculation results:", days.tm_yday)

