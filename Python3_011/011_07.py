#!/usr/bin/evn python3
# coding:utf-8

X = [[12, 7, 3],
     [ 4, 5, 6],
     [ 7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

X_plus_Y=[]

for i in range(len(X)):				# 行
    X_plus_Y.append([])				# “二维”
    for j in range(len(X[i])):		# 列
        X_plus_Y[i].append(X[i][j] + Y[i][j])

print(X_plus_Y)

