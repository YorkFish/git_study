#!/usr/bin/env python3
# coding:utf-8

X = [[12, 7, 3],
     [ 4, 5, 6],
     [ 7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

X_plus_Y = [ i+j for i,j in zip(sum(X,[]), sum(Y,[]))]		# (*)
X_plus_Y = [ X_plus_Y[0:3], X_plus_Y[3:6], X_plus_Y[6:9]]

print(X_plus_Y)

'''
(*) sum() 的小例子
>>> sum(X, [])
[12, 7, 3, 4, 5, 6, 7, 8, 9]
>>> sum(Y, [])
[5, 8, 1, 6, 7, 3, 4, 5, 9]
'''

