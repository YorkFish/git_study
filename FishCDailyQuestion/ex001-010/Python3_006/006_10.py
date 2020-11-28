#!/usr/bin/env python3
# coding:utf-8

'''
 006_08.py 可以做一些变动，这里不做更改
1. input 可以放到 range 中
2. 列表 a 中的内容可以简化，但会使数列不完整
3. 以下是简化 a 后的方案 2
'''

n = int(input("Please enter a number: "))

fib_lst = [ x[0] for x in [ (a[-1], a.append(a[-1]+a[-2])) for a in ( [1,1],) for i in range(n)]]	# (1)
fib_lst.insert(0, 1)																				# (2)
fib_lst.insert(0, 0)																				# (3)
'''
(1) 得到的是这样的：[1, 2, 3, ...]
(2) 与 (3) 是在 (1) 得到的列表前面插入 0, 1 使之变成这样：[0, 1, 1, 2, 3, ...]
'''

print("\nNo.{0} Fibonacci number is {1}.".format(n, fib_list[n-1]))

