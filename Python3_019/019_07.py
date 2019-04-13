#!/usr/bin/env python3
# coding:utf-8

import os.path
#from os import path

fname = input("请输入文件名，不必加后缀：")
fname = "~/Desktop/" + fname + ".txt"						# 偷懒了，测试时少敲几下
if os.path.exists(fname):
    print("文件已经存在！")
else:
    print(fname, "已建好！")
    tmp = []
    while True:
        one_line = input("请输入文件内容，（单独输入“.”为结束）：")
        if one_line == '.':
            print(f"输入完毕，文件 {fname}.txt 已保存！")	# 其实这会儿还没存盘
            break
        else:
            tmp.append(one_line + '\n')
    with open(fname, 'w') as f:
        f.writelines(tmp)

