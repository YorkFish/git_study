#!/usr/bin/env python3
# coding:utf-8

# 对 013_02.py 做了一些改进，减少了 dict 的写操作
def magic(num_dict, k):
    """对 num_dict 使用 k 次魔力"""
    for i in range(k):
        tmp = num_dict['n1']
        for j in range(1, len(num_dict)):
            num_dict[f'n{j}'] += num_dict[f'n{j+1}']
            if num_dict[f'n{j}'] >= 100:
                num_dict[f'n{j}'] %= 100
        num_dict['n5'] += tmp
        if num_dict['n5'] >= 100:
            num_dict['n5'] %= 100

    return num_dict

if __name__ == '__main__':
    # 偷懒～
    # 假装 n = 5; k = 100; 传入数字为 1 2 3 4 5
    n, k = 5, 100
    num_dict = {'n1':1, 'n2':2, 'n3':3, 'n4':4, 'n5':5}
    
    print(magic(num_dict, k))

