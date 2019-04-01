#!/usr/bin/env python3
# coding:utf-8

# 这里不偷懒，一个个自己输入
num_lst = [ int(i) for i in input("Please enter a set of numbers separated by spaces: ").split(' ')]
print("\nThe original order:", num_lst)

# 最值的“绕远路”求法 1
tmp_lst = num_lst[:]		# “替身术”
tmp_lst.sort()				# 排序
num_max = tmp_lst.pop()		# 取出末尾的最大值
num_min = tmp_lst.pop(0)	# 取出首位的最小值

num_lst[num_lst.index(num_max)], num_lst[0] = num_lst[0], num_lst[num_lst.index(num_max)]
num_lst[-1], num_lst[num_lst.index(num_min)] = num_lst[num_lst.index(num_min)], num_lst[-1]

print("\nAfter sorting:", num_lst)

