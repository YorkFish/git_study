#!/usr/bin/env python3
# coding:utf-8

import itertools										# itertools 库 提供用于操作迭代对象的函数

list1 = list(itertools.permutations(range(1, 5), 3))	# permutations 全排列

print(list1)
print("\n总共有 {} 种排列方式。".format(len(list1)))

