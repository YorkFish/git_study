#!/usr/bin/env python3
# coding:utf-8

X = [[12, 7, 3],
     [ 4, 5, 6],
     [ 7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

def matrix_plus(X, Y):
    if len(X) == len(Y):		# 阶数相同才可相加（不过此处没判断列）
        X_plus_Y = []
        for i in range(len(X)):
            tmp = []
            for a,b in zip(X[i], Y[i]):
                tmp.append(a+b)
            X_plus_Y.append(tmp)
        return X_plus_Y
    else:
        print("X and Y cannot be added together.")

print(matrix_plus(X, Y))

