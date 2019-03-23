#!/usr/bin/env python3
# coding:utf-8

# 改进 003_10.py
from math import sqrt

for i in range(-100, 10001):
    str1 = str(sqrt(i + 100))
    str2 = str(sqrt(i + 268))
    if len(str1) <= 5 and len(str2) <= 5:
        print(i)

