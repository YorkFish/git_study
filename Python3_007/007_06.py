#!/usr/bin/env python3
# coding:utf-8

# “直角三角形”输出
# 此程序是对 007_05.py 的改进；加入了换行，但有违 Python 简洁的思想
print('\n'.join( ['  '.join([ '%d x %d = %2d' % (j, i, i*j) for j in range(1, i+1)]) for i in range(1, 10)]))	# (*)
# print('\n'.join( '  '.join([ '%d x %d = %2d' % (j, i, i*j) for j in range(1, i+1)]) for i in range(1, 10))) 也行

'''
(*) 可以这样理解
lst1 = []
for i in range(1, 10):			# i 控制行
    lst2 = []
    for j in range(1, i+1):		# j 控制列
        lst2.append('%d x %d = %2d' % (j, i, i*j))
    lst1.append('  '.join(lst2))

print('\n'.join(lst1))
'''

