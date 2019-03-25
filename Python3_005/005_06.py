#!/usr/bin/env python3
# coding:utf-8

num_lst = [ int(num) for num in input("input x-y-z: ").split('-')]
new_lst = []

# while 版本
i, tmp = 3, 0
while i > 0:
    tmp = min(num_lst)
    new_lst.append(tmp)
    num_lst.remove(tmp)
    i -= 1

'''
for 版本
for i in rnage(3):
    tmp = min(num_lst)
    new_lst.append(tmp)
    num_lst.remove(tmp)
'''

print("\nThe order from small to large is:", new_lst)

