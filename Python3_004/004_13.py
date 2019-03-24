#!/usr/bin/env python3
# coding:utf-8

from datetime import datetime

year, month, day = int(input("year:  ")), int(input("month: ")), int(input("day:   "))
print( list( datetime(year, month, day).timetuple())[-2])

