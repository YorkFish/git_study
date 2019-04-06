#!/usr/bin/env python3
# coding:utf-8

# 此法结合了 017_01.py 与 017_03.py
array = [-66, -33, 0, 99, 11, 55, 22, -44, 77, -88]		# 偷个懒~
array.sort()
diff_min = abs(array[1] - array[0])
for i in range(1, len(array)-1):		# 因为 diff_min 的初值，所以略去一次运算
    if diff_min > array[i+1] - array[i]:
        diff_min = array[i+1] - array[i]

print("\nMinimum difference is:", diff_min)

