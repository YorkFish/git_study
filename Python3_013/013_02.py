#!/usr/bin/env python3
# coding:utf-8

def new_dict(num_dict):
    """ “循环左移” 1 格，并存入新字典"""
    tmp_dict = {}
    n = len(num_dict)
    for i in range(1, n):
        tmp_dict[f'n{i}'] = num_dict[f'n{i+1}']		# format 的另一种用法
    tmp_dict[f'n{n}'] = num_dict[f'n{1}']

    return tmp_dict

def magic(num_dict, k):
    """对 num_dict 使用 k 次魔力"""
    tmp_dict = {}
    for i in range(k):
        tmp_dict = new_dict(num_dict)
        for j in range(1, len(num_dict)+1):
            num_dict[f'n{j}'] += tmp_dict[f'n{j}']
            if num_dict[f'n{j}'] >= 100:
                num_dict[f'n{j}'] -= 100			# 正常情况下 -100 与 %100 效果一样

    return num_dict

if __name__ == '__main__':
    # 偷懒～
    # 假装 n = 5; k = 100; 传入数字为 1 2 3 4 5
    n, k = 5, 100
    num_dict = {'n1':1, 'n2':2, 'n3':3, 'n4':4, 'n5':5}

    print(magic(num_dict, k))

