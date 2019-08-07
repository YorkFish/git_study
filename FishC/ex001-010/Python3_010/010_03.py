#!/usr/bin/env python3
# coding:utf-8

fun = lambda x: (x + 1) * 2
x = 1
for i in range(1, 10):		# 第 1 天开始吃，第 10 天没吃
    x = fun(x)				# 倒推

print("There are {} peaches in all.".format(x))

