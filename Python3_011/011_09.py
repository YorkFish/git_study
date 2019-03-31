#!/usr/bin/env python3
# coding:utf-8

X = [[12, 7, 3],
     [ 4, 5, 6],
     [ 7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

# 此函数是对 011_08.py 的改进
def matrix_plus(X, Y):  
    if len(X) != len(Y):	# 判断行
        return "X and Y cannot be added together."
    else:					# 判断列
        raw = 0
        for i in X:
            if len(i) != len(Y[raw]):
                return "X and Y cannot be added together."
            else:
                raw += 1
    
    X_plus_Y = []
    for i in range(len(X)):
        tmp = []
        for a,b in zip(X[i], Y[i]):
            tmp.append(a+b)
        X_plus_Y.append(tmp)
    
    return X_plus_Y

print(matrix_plus(X, Y))

'''
matrix_plus() 中的判断语句可以这样改进
if len(X) != len(Y):
	return "X and Y cannot be added together."
else:
	for i,j in zip(X, Y):
		if len(i) != len(j):
			return "X and Y cannot be added together."

ps: 其实还有漏洞，因为同一个矩阵的列是定长
'''

