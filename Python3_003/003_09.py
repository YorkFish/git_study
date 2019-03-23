#!/usr/bin/env python3
# coding:utf-8

'''
(i^2-100)  <-  -100  <-  (i^2)  ->  +168  ->  (j^2)
借鉴 004_08.py 可知
 0 <= i <= 83
13 <= j <= 84
'''
for i in range(84):
    for j in range(13, 85):
        if(j**2 - i**2) == 168:
            print(i**2 - 100)
            break				# 不做无谓的的计算

