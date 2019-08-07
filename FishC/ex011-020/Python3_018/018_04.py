#!/usr/bin/env python3
# coding:utf-8

# for + print()
lst = input("请输入一组数字，并用空格隔开： ").split()
for i in range(len(lst)-1, -1, -1):
    print(lst[i], end=' ')

