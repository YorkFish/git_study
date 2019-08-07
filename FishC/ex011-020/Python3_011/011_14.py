#!/usr/bin/env python3
# coding:utf-8

import numpy as np

X = np.mat([[12, 7, 3],
            [ 4, 5, 6],
            [ 7, 8, 9]])	# mat 代表二维矩阵

Y = np.mat([[5, 8, 1],
            [6, 7, 3],
            [4, 5, 9]])

print(X + Y) 

