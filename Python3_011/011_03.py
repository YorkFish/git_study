#!/usr/bin/env python3
# coding:utf-8

X = [[12, 7, 3],
     [ 4, 5, 6],
     [ 7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

# 下方程序是对 011_02.py 的改写
X_plus_Y = []

# 记下方的 for 循环为 (*)
for raw in range(3):
    X_plus_Y.append([ X[raw][col]+Y[raw][col] for col in range(3)])

print(X_plus_Y)

'''
(*) 还能这样改
X_plus_Y.append([ [ X[raw][col]+Y[raw][col] for col in range(3)] for raw in range(3)])
'''

