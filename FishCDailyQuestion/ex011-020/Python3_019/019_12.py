#!/usr/bin/env python3
# coding:utf-8

# 此法权当拓展思路
import os, sys

fn = input("请输入文件名，不必加后缀：")
fn += ".txt"
os.chdir("~/Desktop/")

if os.path.exists(fn):
    print("文件已经存在!")
    sys.exit()			# 退出脚本

with open(fn, 'w+') as f:
    while True:
        one_line = input("请输入内容，（单独输入“.”为结束）：")
        if one_line != '.':
            f.write(one_line + '\n')
            continue
        else:
            f.flush()	# 强行把缓冲区中的内容放到磁盘中
            break

