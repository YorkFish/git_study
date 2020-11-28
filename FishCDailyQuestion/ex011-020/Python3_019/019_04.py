#!/usr/bin/env python3
# coding:utf-8

p = "~/Desktop/"
name = input("请输入文件名，并加上后缀：")
try:
    f = open(p+name, 'r')		# r: 默认值，可不写；只读模式打开；如果文件不存在，返回异常 FileNotFoundError
    print("该文件已存在")
except FileNotFoundError:		# 'r' 的异常
    f = open(p+name, 'w')		# 此处的 'w' 可换成 'x' 或 'a'
    one_line = input("请输入内容，输入“.”结束：")
    while one_line != '.':
        f.write(one_line + '\n')
        one_line = input("请继续输入内容，直到“.”即可结束：")
finally:
    print("文件已保存！")
    f.close()

