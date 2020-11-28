#!/usr/bin/env python3
# coding:utf-8

# 本程序是对 015_01.py 的“缩写”
n = int(input("Please enter a number: "))
tale = sum([ 1/i for i in range(1 if n%2 else 2, n+1, 2)])
print('+'.join([ '1/'+str(i) for i in range( 1 if n%2 else 2,n+1,2)]), '=', tale)

