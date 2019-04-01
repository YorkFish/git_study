#!/usr/bin/env python3
# coding:utf-8

# 这里不偷懒，一个个自己输入
num_lst = [ int(i) for i in input("Please enter a set of numbers separated by spaces: ").split(' ')]
print("\nThe original order:", num_lst)

# 最值的“绕远路”求法 2
max_idx, min_idx = 0, 0
max_tmp, min_tmp = num_lst[0], num_lst[0]
for i in range(len(num_lst)):
    if max_tmp < num_lst[i]:
        max_tmp = num_lst[i]
        max_idx = i
    elif min_tmp > num_lst[i]:
        min_tmp = num_lst[i]
        min_idx = i

num_lst[max_idx], num_lst[0] = num_lst[0], num_lst[max_idx]
num_lst[-1], num_lst[min_idx] = num_lst[min_idx], num_lst[-1]

print("\nAfter sorting:", num_lst)

