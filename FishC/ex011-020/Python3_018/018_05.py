#!/usr/bin/env python3
# coding:utf-8

# 此法相当于 018_04.py 的 while 版
# while + pirnt()
lst = input("请输入一组数字，并用空格隔开： ").split()

i = -1
while i >= -len(lst):
    print(lst[i], end=' ')
    i -= 1

