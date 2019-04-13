#!/usr/bin/env python3
# coding:utf-8

p = "~/Desktop/"
try:
    with open(p+input("请输入文件名，并加上后缀："), 'x') as f:
        while True:
            one_line = input("请输入内容，直到“.”结束：")
            if one_line != '.':
                f.write(one_line + '\n')
            else:
                break
except FileExistsError:		# 'x' 的异常
    print("文件已存在！")

