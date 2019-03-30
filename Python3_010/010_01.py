#!/usr/bin/env python3
# coding:utf-8

def calc(x):
    return (x + 1) * 2

def peach(day):
    t = 1
    for i in range(1, day):
        t = calc(t)
        # print("第 {} 天吃之前，有 {:>4} 个桃子。".format(day-i, t))
    
    return t

print("There are {} peaches in all.".format(peach(10)))

'''
说白了就是
x = 1
for i in range(9):		# 吃了 9 次
    x = 2 * (x + 1)
print("There are {} peaches in all.".format(x))
'''

