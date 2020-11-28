#!/usr/bin/env python3
# coding:utf-8

x, y, z = [ int(num) for num in input("Please enter x-y-z(e.g. 1-2-3): ").split('-')]

# 使结果按 x < y < z 的形式排列
if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y

print("\nThe order from small to large is: {0}, {1}, {2}".format(x, y, z))

