#!/usr/bin/env python3
# coding:utf-8

X = [[12,7,3],
     [4,5,6],
     [7,8,9]]

Y = [[5,8,1],
     [6,7,3],
     [4,5,9]]

def matrix_plus(X, Y):
    X_plus_Y = [ list(zip(X[i],Y[i])) for i in range(len(X))]	# (*)
    for i in range(len(X)):										# 行
        for j in range(len(X[0])):								# 列
            X_plus_Y[i][j] = sum(X_plus_Y[i][j])
    return X_plus_Y

print(matrix_plus(X, Y))

'''
(*) 加个小例子
>>> list(zip(X[0], Y[0]))
[(1, 9), (2, 8), (3, 7)]
'''

