#!/usr/bin/env python3
# coding:utf-8

p = "~/Desktop/"
name = input("请输入文件名，并加上后缀：")
try:
    with open(p+name, 'x') as f:
        tmp = []
        while True:
            text = input("请继续输入内容，直到“.”结束：")
            if text == '.':
                f.writelines(tmp)		# 将列表 tmp 的各元素连接起来写入文件
                print("文件已保存！")
                break
            else:
                tmp.append(text + '\n')
except FileExistsError:					# 'x' 的异常
    print('此文件已存在！')

