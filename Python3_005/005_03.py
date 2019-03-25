#!/usr/bin/env python3
# coding:utf-8

sort_lst = []
for i in range(1, 4):			# 多了一种输入的方法
    sort_lst.append( input("Please enter No." + str(i) + " number: "))
	# sort_lst.append( int(input("Please enter No." + str(i) + " number: "))) 也行，但多次一举了
'''
或者
for i in range(1, 4):
    sort_lst.append( input("Please enter No.{} number: ".format(i)))

或者
for i in range(3):
    sort_lst.append( input("Please enter No." + str(i+1) + " number: "))
'''

x, y, z = sorted(sort_lst)		# 多了一种赋值的方法
'''
lst.sort() 是给 lst 排序，会破坏 lst 的结构
sorted(lst) 是产生一个副本并排序，不破坏 lst 的结构
'''

print("\nThe order from small to large is: {0}, {1}, {2}".format(x, y, z))
# print("\nThe order from small to large is: {}, {}, {}".format(x, y, z)) 也行

