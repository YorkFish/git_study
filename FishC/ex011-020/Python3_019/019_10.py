#!/usr/bin/env python3
# coding:utf-8

import os

fn = input("请输入文件名，不必加后缀：")
fn +=  ".txt"					# 偷懒了，测试时少敲几下
p = "~/Desktop/"

os.chdir(p)

if os.path.exists(fn):			# 在路径中检查 fn 是否存在
    print(fn, "已经存在！")
else:
    pf = os.path.join(p, fn)	# 在路径中添加 fn
    with open(pf, 'w') as f:
        while True:
            one_line = input("请输入内容，（单独输入“.”为结束）：")
            if one_line != '.':
                f.write("%s\n" % one_line)
            else:
                print(fn, "已经保存！")
                break

