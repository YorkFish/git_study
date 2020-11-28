#!/usr/bin/env python3
# coding:utf-8

from random import randint

array = [ randint(-100, 100) for i in range(10)]
print("The initial array is:", array)

array.sort()
print("\nMinimum difference is:", min([ abs(array[i]-array[i+1]) for i in range(9)]))	# (*)

'''
(*) 可用以下几种方式取代

# 1. 因为已经排好序，用大的减小的即可
(solution 1) min([ array[i]-array[i-1] for i in range(1, 10)])

(solution 2) min( array[i+1]-array[i] for i in range(9))

# 2. 先排序 sort()，再倒序 reverse()；或 sort(reverse=True)，然后依次比较即可
min([ array[i]-array[i+1] for i in range(9)])

# 3. 用小的减大的也行，最后去个相反数即可
'''

