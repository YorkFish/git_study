#!/usr/bin/env python3
# coding:utf-8

array1 = [-66, -33, 0, 99, 11, 55, 22, -44, 77, -88]	# 偷个懒~
array2 = []

while len(array1) > 1:
    for i in array1[1:]:
        array2.append(abs(array1[0] - i))
    array1.pop(0)

print("Minimum difference is:", min(array2))

