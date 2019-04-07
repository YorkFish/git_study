#!/usr/bin/env python3
# coding:utf-8

# for + insert()
lst1 = input("请输入一组数字，并用空格隔开： ").split()
lst2 = []
for i in range(lst1):
    lst2.insert(0, i)

print(' '.join(lst2))

