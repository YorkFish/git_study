#!/usr/bin/env python3
# coding:utf-8

# 此法适用多个数
num_lst = [ int(num) for num in input("Please enter x-y-z(e.g. 1-2-3): ").split('-')]

num_lst.sort()		# 给列表按“从小到大”的顺序排序

print("\nThe order from small to large is: {0}, {1}, {2}".format(num_lst[0], num_lst[1], num_lst[2]))

