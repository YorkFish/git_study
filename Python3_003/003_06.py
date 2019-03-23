#!/usr/bin/env python3
# coding:utf-8

from math import sqrt

# 思路与 003_05.py 相同
for i in range(84):			# i 的下限为 0，上限为 83
    if sqrt(i * i + 168) % 1 == 0:
        print(i * i - 100)

