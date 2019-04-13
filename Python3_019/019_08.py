#!/usr/bin/env python3
# coding:utf-8

import os

p = "~/Desktop/"
os.chdir(p)				# 更改路径
lst = os.listdir()		# 将当前路径下的文件名存入 lst

fname = input("请输入文件名，不必加后缀：")
fname += ".txt"			# 偷懒了，测试时少敲几下
if fname in lst:
    print(fname, "已经存在!")
else:
    pf = p + fname
    f = open(pf, 'w')
    while True:
        one_line = input("请输入内容，（单独输入“.”为结束）：")
        if one_line == '.':
            f.close()
            print("文件已保存！")
            break
        f.write(one_line + '\n')

