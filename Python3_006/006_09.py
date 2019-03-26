#!/usr/bin/env python3
# coding:utf-8

'''
 006_08.py 可以做一些变动
1. input 可以放到 range 中，这里不做更改
2. 列表 a 中的内容可以简化，但会使数列不完整
3. 以下是简化 a 后的方案 1
'''

n = int(input("Please enter a number: "))

if n < 3:
    fib_lst = [0, 1, 1]
    print("\nNo.{0} Fibonacci number is {1}.".format(n, fib_lst[n-1]))
else:
    fib_lst = [ x[0] for x in [ (a[-1], a.append(a[-1]+a[-2])) for a in ( [1,1],) for i in range(n)]]	# (*)
    print("\nNo.{0} Fibonacci number is {1}.".format(n, fib_lst[n-3]))

'''
1. (*) 可以这样理解
lst = []
for a in ( [1,1],):
    for i in range(n):
        lst.append( (a[-1], a.append(a[-1]+a[-2])))
fib_lst = []
for x in lst:
    fib_lst.append(x[0])

2. (*)也可以这样理解
a = [1, 1]
lst = []
for i in range(n):
    lst.append( (a[-1],  None))
    a.append(a[-1]+a[-2])
fib_lst = []
for x in lst:
    fib_lst.append(x[0])
print(fib_lst)
'''

