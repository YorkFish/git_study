#!/usr/bin/python3
# coding:utf-8

import itertools as it		# 导入 itertools 库

list1 = [ i for i in it.permutations(range(1, 5), 3)]

print(list1)
print("\n总共有 {} 种排列方式。".format(len(list1)))

