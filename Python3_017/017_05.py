#!/usr/bin/env python3
# coding:utf-8

# 此法结合了 017_02.py 与 017_03.py
def get_min(arr):
    sorted_arr = sorted(arr)
    tmp = []
    for i in range(10):
        #print(sorted_arr[i] - sorted_arr[i-1], end=' ')	
        tmp.append( abs(sorted_arr[i] - sorted_arr[i-1]))	# (*)
    
    return min(tmp)

array = [-66, -33, 0, 99, 11, 55, 22, -44, 77, -88]			# 偷懒~
print("\nMinimum difference is:", get_min(array))

'''
(*) 处代码可以首尾相减，但此题没必要用
一般情况下，首尾肯定“相距最远”
数字一样时，也没必要首尾相减
'''

