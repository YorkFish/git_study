#!/usr/bin/env python3
# coding:utf-8

# list[::-1]
lst = input("请输入一组数字，并用空格隔开： ").split()
print(' '.join(lst[::-1]))		# 用 lst[-1::-1] 也行

'''
# 一行版
print(' '.join( input("请输入一组数字，并用空格隔开： ").split()[::-1]))
'''

