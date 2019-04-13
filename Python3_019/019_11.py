#!/usr/bin/env python3
# coding:utf-8

# 此法权当拓展思路
import os

p = "~/Desktop/"
fn = input("请输入文件名，不必加后缀：")
fn += ".txt"

files = os.walk(p)		# 这里“割鸡用牛刀了”

for i in files:			# 把子目录（若有）也检查了，“突破”了题意
    for j in i[2]:		# i[0]: 路径 i[1]: 文件夹 i[2]: 文件
        if j == fn:
            print("文件已经存在！")
            break
else:
    pf = p + fn
    f = open(pf, 'w')
    one_line = input("请输入内容（单独输入“.”为结束）：")
    while one_line != '.':
        f.write(one_line)
        one_line = input("请输入内容（单独输入“.”为结束）：")
    f.close()
	print(fn, "文件已保存！")

