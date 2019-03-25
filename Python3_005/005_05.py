#!/usr/bin/env python3
# coding:utf-8

num_lst = [ int(num) for num in input("Please enter x-y-z(e.g. 1-2-3): ").split('-')]

'''
其实下面就是“选择排序”
总共比较 3 次
{0}{1}{2}
    {0} 与 {1} 比
    {0} 与 {2} 比
    {1} 与 {2} 比
'''
# for 版本
for i in range(2):
    for j in range(i+1, 3):
        if num_lst[i] > num_lst[j]:
            num_lst[i] ,num_lst[j] = num_lst[j], num_lst[i]

'''
for + while 版本
for i in range(2):
    j = i + 1
    while j < 3:
        if num_lst[i] > num_lst[j]:
            num_lst[i], num_lst[j] = num_lst[j], num_lst[i]
        j += 1
'''

print("\nThe order from small to large is:", num_lst)

