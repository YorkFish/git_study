#!/usr/bin/env python3
# coding:utf-8

X = [[12, 7, 3],
     [ 4, 5, 6],
     [ 7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

X_plus_Y = X.copy()		# (*)

for i in range(3):
    for j in range(3):
        X_plus_Y[i][j] += Y[i][j]

print(X_plus_Y)

'''
(*) 的另一种写法 1
import copy
X_plus_Y = copy.deepcopy(X)

(*) 的另一种写法 2
X_plus_Y = X[:]
'''

