#!/usr/bin/env python3
# coding:utf-8

# 半成品，没有换行
print('  '.join([ '%d x %d = %2d' % (j, i, i*j) for i in range(1, 10) for j in range(1, i+1)]))		# (*)

'''
(*) 可以这样理解
lst = []
for i in range(1, 10):			# i 控制行
    for j in range(1, i+1):		# j 控制列
        lst.append('%d x %d = %2d' % (j, i, i*j))
print('  '.join(lst))
'''

