#!/usr/bin/env python3
# coding:utf-8

try:
    fname = input("请输入文件名，不必加后缀：")
    fname = "~/Desktop/" + fname + ".txt"		# 偷懒了，测试时少敲几下
    f = open(fname, 'r')
    print("此文件已经存在!")
except FileNotFoundError:						# 'r' 的异常
    f = open(fname, 'w')
    print(fname + "已建好")
    one_line = input("请输入内容，（单独输入“.”为结束）：")
    while one_line != '.':
        f.write(one_line + '\n')
        one_line = input("请继续输入内容，（单独输入“.”为结束）：")
    print("文件已保存！")
finally:
    f.close()

