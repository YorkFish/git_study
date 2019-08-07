#!/usr/bin/env python3
# coding:utf-8

array = [-66, -33, 0, 99, 11, 55, 22, -44, 77, -88]				# 偷个懒~
print(min( abs(i-j) for i in array for j in array if i != j))	# 此处有一半是重复操作

