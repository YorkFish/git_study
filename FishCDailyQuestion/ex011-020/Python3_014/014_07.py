#!/usr/bin/env python3
# coding:utf-8

def get_num(num_lst):
    global count					# count 是循环的重点
    if len(num_lst) == 1:			# num_lst=1 的时候，剩下的是答案
        print("\nThe lucky number is:", num_lst[0])
    else:
        length = len(num_lst)
        for i in range(length):
            if count == 3:			# 数到 3 出场
                num_lst[i] = 0
                count = 1
            else:
                count += 1
        for j in range(length-1, -1, -1):
            if num_lst[j] == 0:		# 删除退出的值；把非零值加到新列表也行
                del num_lst[j]

        get_num(num_lst)			# 数组已经改变，重新调用一次函数，此时 count 不变

def run():
    n = int(input("Please enter a number of people: "))
    num_lst = list( range(1, n+1))
    get_num(num_lst)

if __name__ == '__main__':
    count = 1
    run()

