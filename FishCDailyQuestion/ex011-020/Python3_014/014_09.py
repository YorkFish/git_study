#!/usr/bin/env python3
# coding:utf-8

def get_num(n, num_lst):
    for i in range(n-1):	# (*)
        for j in range(3):
            tmp = num_lst[0]
            num_lst.remove(tmp)
            if j != 2:
                num_lst.append(tmp)
    
    print("\nThe lucky number is:", num_lst[0])
'''
(*) 的另一种写法
for i in range(n-1):
    for j in range(2):
        num_lst.append(num_lst.pop(0))
    num_lst.pop(0)
'''

def run():
    n = int(input("Please enter the number of people: "))
    num_lst = [ i for i in range(1, n+1)]
    get_num(n, num_lst)

if __name__ == '__main__':
    run()

