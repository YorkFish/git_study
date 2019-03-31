#!/usr/bin/env python3
# coding:utf-8

X = [[12, 7, 3],
     [ 4, 5, 6],
     [ 7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

# 011_04.py 的另一种写法 1

print([ [ sum(col) for col in zip(raw[0],raw[1])] for raw in zip(X,Y)])		# (*)

'''
(*) 写开来，即
lst1 = []
for raw in zip(X, Y):
    lst2 = []
    for col in zip(raw[0], raw[1]):
        lst2.append(sum(col))
    lst1.append(lst2)

print(lst1)
'''

'''
(*) zip 小例子
>>> list(zip([1, 2, 3], [9, 8, 7]))
[(1, 9), (2, 8), (3, 7)]
'''

