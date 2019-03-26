#!/usr/bin/env python3
# coding:utf-8

n = int(input("Please enter a number: "))

fib_lst = [ x[0] for x in [ (a[i][0], a.append( (a[i][1], a[i][0]+a[i][1]))) for a in ( [[0,1]],) for i in range(n)]]	# (*)
'''
1. (*) 可以这样理解
for a in ( [[0, 1]],):
    for i in range(n):
        a.append( (a[i][1], a[i][0]+a[i][1]))
fib_lst = []
for x in a:
    fib_lst.append(x[0])

2. (*)也可以这样理解
a = [ [0, 1]]
for i in range(n):
    a.append( (a[i][1], a[i][0]+a[i][1]))
fib_lst = []
for x in a:
    fib_lst.append(x[0])
'''

print("\nNo.{0} Fibonacci number is {1}.".format(n, fib_lst[-1]))

