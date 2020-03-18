#!/usr/bin/env python3
# coding:utf-8

f = open("yankeedoodle.csv")
nums = [num.strip() for num in f.read().split(',')]
f.close()
res = [int(x[0][5] + x[1][5] + x[2][6]) for x in zip(nums[0::3], nums[1::3], nums[2::3])]
print(''.join([chr(e) for e in res]))
