#!/usr/bin/env python3
# coding:utf-8

def get_num(n):
    lst = list( range(1, n+1))
    
    def cal(lst, mod):
        """闭包中，lst 是剩余的人的列表，mod 是每一圈从哪开始的信息"""
        if len(lst) == 1:
            print("\nThe lucky number is:", lst[0])
        else:
            tmp = (len(lst) + mod) % 3										# 上一代的“恩怨”（如果有），算到这一代“头上”
            new_lst = list( filter(lambda x: x not in lst[2-mod::3], lst))	# 逢 3 过滤

            return cal(new_lst, tmp)
    
    return cal(lst, 0)
'''
filter(function, iterable)
    function -- 判断函数
    iterable -- 可迭代对象

filter() 用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象
它接收两个参数，第一个为函数，第二个为序列
序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中
'''

if __name__ == '__main__':
    n = int(input("Please enter a number of people: "))
    get_num(n)

