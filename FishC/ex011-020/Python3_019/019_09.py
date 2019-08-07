#!/usr/bin/env python3
# coding:utf-8

import os

fname = input("请输入文件名，不必加后缀：")
fname += ".txt"				# 偷懒了，测试时少敲几下，下面也是
pf = "~/Desktop/%s" % fname

if os.path.isfile(pf):		# 判断文件与否；存在则返回 True
	print(fname, "已经存在！")
else:
	with open(pf, 'w') as f:
		while True:
			one_line = input("请输入内容，（单独输入“.”为结束）：")
			if one_line != ".":
				f.write(one_line + '\n')
			else:
                print(fname, "已经保存！")
                break

