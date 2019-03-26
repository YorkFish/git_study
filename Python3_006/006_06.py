#!/usr/bin/env python3
# coding:utf-8

def fib(n):
    yield 0
    x, y = 0, 1
    yield x
    for i in range(n-1):
        x, y = y, x + y
        yield x
'''
fib() 可以简化
简化 1
def fib(n):
    x, y = 0, 1
    for i in range(n):
        yield x
        x, y = y, x + y

简化 2
def fib(n):
    x, y = 0, 1
    for i in range(n-1):
        x, y = y, x + y
        yield x
'''

n = int(input("Please enter a number: "))
fib_lst = []
for i in fib(n):
    fib_lst.append(i)

print("\nNo.{0} Fibonacci number is {1}.".format(n, fib_lst[-1]))

'''
yield 表达式在定义生成器函数或异步生成器函数时使用，并且只能在函数定义的主体中使用
在函数体中使用 yield 表达式会使得该函数成为生成器

官网找的例子
>>> def echo(value=None):
...     print("Execution starts when 'next()' is called for the first time.")
...     try:
...         while True:
...             try:
...                 value = (yield value)
...             except Exception as e:
...                 value = e
...     finally:
...         print("Don't forget to clean up when 'close()' is called.")
...
>>> generator = echo(1)
>>> print(next(generator))
Execution starts when 'next()' is called for the first time.
1
>>> print(next(generator))
None
>>> print(generator.send(2))
2
>>> generator.throw(TypeError, "spam")
TypeError('spam',)
>>> generator.close()
Don't forget to clean up when 'close()' is called.
'''

