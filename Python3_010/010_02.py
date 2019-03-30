#!/usr/bin/env python3
# coding:utf-8

def peach(n):
    '''
    n: 前一天剩下的数量
    n=10 时，桃子总数浮出水面
    '''
    if n == 1:
        return 1
    else:			# 不用 else 也行，return 注意缩进即可
        return (peach(n-1) + 1) * 2

print("There are {} peaches in all.".format(peach(10)))

