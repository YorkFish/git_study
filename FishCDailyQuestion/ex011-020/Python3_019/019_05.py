#!/usr/bin/env python3
# coding:utf-8

def new_file():
    fname = input("请输入文件名，并加上后缀：")
    p = "~/Desktop/" + fname
    try:
        f = open(p, 'r')
    except Exception as e:	# 接受异常，然后可以把这个 e 打印出来
        print(e)
        print(fname + "已建好")
        f = open(p, 'w')
        one_line = input("请输入内容，（单独输入“.”为结束）：")
        while one_line != '.':
            f.write(one_line + '\n')
            one_line = input("请继续输入内容，（单独输入“.”为结束）：")
        print("文件已保存！")
    else:
        print("此文件已存在！")

if  __name__=='__main__':
    new_file()

