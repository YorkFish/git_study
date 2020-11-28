#!/usr/bin/evn python3
# coding:utf-8

'''
找规律
                     1
                4 =  1 +  3		# num = 1, tmp = 3
          10 =  4 +  6			# num = 4, tmp = 6
     22 = 10 + 12
46 = 22 + 24
把乘法转换成了加法
'''

num, tmp = 1, 0					# tmp 可以不赋初值
for i in range(1, 10):
    tmp = num + 2
    num += tmp

print("There are {} peaches in all.".format(num))

