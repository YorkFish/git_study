#!/usr/bin/env python3
# coding:utf-8

'''
此法权当拓展思路
因为这个程序绕了远路
不过可以借此复习一下
random, copy(), min(), index(), append(), remove() ...
'''
from random import randint

num_lst = [ randint(1, 100) for i in range(3)]	# 懒得想输入的数字
print("Original list:", num_lst)

tmp_lst = num_lst.copy()
new_lst = []

for i in range(3):
    num_min = min(tmp_lst)						# 找出当前过渡列表的最小值
    idx = num_lst.index(num_min)				# 得到当前最小值在原列表的下标
    new_lst.append(idx)							# 把下标添加到目标列表中
    tmp_lst.remove(num_min)						# 删除过渡列表中的当前最小值

# 就算原列表生成的随机数字有重复也不影响结果
for i in new_lst:
    print(num_lst[i], end=' ')

