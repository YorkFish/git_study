#!/usr/bin/env python3
# coding:utf-8

# for + pop()
lst = input("请输入一组数字，并用空格隔开： ").split()
for i in range(len(lst)):
    print(lst.pop(), end=' ')

