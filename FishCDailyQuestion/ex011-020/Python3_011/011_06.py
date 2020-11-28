#!/usr/bin/env python3
# coding:utf-8

X = [[12, 7, 3],
     [ 4, 5, 6],
     [ 7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

# 011_04.py 的另一种写法 2
print([ [ x+y for x,y in zip(X[raw],Y[raw])] for raw in range(len(X))])		# (*)

'''
(*) 写开来，即
lst1 = []
for raw in range(len(X)):
    lst2 = []
    for x,y in zip(X[raw], Y[raw]):
        lst2.append(x + y)
    lst1.append(lst2)

print(lst1)
'''

