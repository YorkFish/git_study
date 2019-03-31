#!/usr/bin/env python3
# coding:utf-8

X = [[12, 7, 3],
     [ 4, 5, 6],
     [ 7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

X_plus_Y = [ [0, 0, 0], [0, 0, 0], [0, 0, 0]]

for raw in range(3):		# 行
    for col in range(3):	# 列
        X_plus_Y[raw][col] = X[raw][col] + Y[raw][col]

print(X_plus_Y)

