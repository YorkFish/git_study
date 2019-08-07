#!/usr/bin/env python3
# coding:utf-8

def is_out_range(num_lst):
    """检验 num_lst 中的每个数字 n 是否都满足 0 <= n <= 99"""
    for i in num_lst:
        if i<0 or i>99:
            return False
    return True

def magic(num_lst, time):
    """对 num_lst 使用 time 次魔力"""
    n = len(num_lst)
    for i in range(time):
        tmp = num_lst[0]
        for j in range(n):
            if j < n-1:
                num_lst[j] += num_lst[j+1]
            elif j == n-1:
                num_lst[j] += tmp
            if num_lst[j] >= 100:
                num_lst[j] %= 100

    return num_lst

def enter_line1():
    """
    输入第一行，并检验
    2 <= n <= 50
    1 <= k <= 2,000,000,000
    """
    lst = [ int(i) for i in input("Please enter n and k(e.g. 5 20): ").split()]	# 尽量使用英文状态的空格；不要以空格结尾
    n, k = lst[0], lst[1]
    while n<2 or n>50 or k<1 or k>2000000000:
	    lst = [ int(i) for i in input("Input error, please enter again: ").split()]
	    n, k = lst[0], lst[1]
    
    return n, k

def enter_line2(num):
    """
    输入第二行，并检验
    0 <= lst[each] <= 99
    """
    lst = [ int(j) for j in input("Please input "+str(num)+" numbers(e.g. 0 2 4): ").split()]
    while len(lst) != num or is_out_range(lst) == False:
        lst = [ int(j) for j in input("Input error, please enter again: ").split()]
    
    return lst

if __name__ == '__main__':
    
    n, k = enter_line1()
    lst = enter_line2(n)
    print(magic(lst, k))

