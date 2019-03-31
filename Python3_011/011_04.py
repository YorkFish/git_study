#!/usr/bin/env python3
# coding:utf-8

X = [[12, 7, 3],
     [ 4, 5, 6],
     [ 7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

# 此程序是对 011_03.py 的改进，3 阶以外的矩阵也能运算
print([ [ X[raw][col]+Y[raw][col] for col in range(len(X[raw]))] for raw in range(len(X))])	# (*)

'''
(*) 写开来，即
lst1 = []
for raw in range(len(X)):
    lst2 = []
    for col in range(len(X[raw])):
        lst2.append(X[raw][col] + Y[raw][col])
    lst1.append(lst2)

print(lst1)
'''

