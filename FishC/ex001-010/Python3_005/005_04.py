#!/usr/bin/env python3
# coding:utf-8

num_lst = [ int(num) for num in input("Please enter x-y-z(e.g. 1-2-3): ").split('-')]

'''
其实下面就是“冒泡排序”
总共比较 3 次
{0}{1}{2}
    {0} 与 {1} 比
    {1} 与 {2} 比
    {0} 与 {1} 比
'''
# for 版本
for i in range(2):
    for j in range(2-i):
        if num_lst[j] > num_lst[j+1]:
            num_lst[j], num_lst[j+1] = num_lst[j+1], num_lst[j]

'''
for + while 版本
for i in range(1, 3):
    while num_lst[i-1] > num_lst[i]:
        num_lst[i-1], num_lst[i] = num_lst[i], num_lst[i-1]
        i -= 1
        if i == 0:
            break
'''

print("\nThe order from small to large is:", num_lst)

