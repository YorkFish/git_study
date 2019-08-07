#!/usr/bin/env python3
# coding:utf-8

try:
    name = input("请输入文件名，不必加后缀：")
    p = "~/Desktop/"					# (*)
    f = open(p+name+".txt", "x")		# x: 创建写模式；文件不存在则创建；存在则返回异常 FileExistsError
    one_line = input("请输入内容，输入“.”结束：")
    while one_line != ".":
        f.write(one_line + '\n')
        one_line = input("请继续输入内容，直到“.”结束：")
    f.close()
except FileExistsError:
    print("此文件已经存在！")

'''
(*) 处路径的几种写法

p = "C:\\Users\\york\\Desktop\\"	# windows 指定路径写法 1
p = r"C:\Users\york\Desktop\"		# windows 指定路径写法 2
p = "C:/Users/york/Desktop/"		# windows 指定路径写法 3

p = "/home/york/Desktop/"			# Linux   指定路径写法 1
p = "~/Desktop/"					# Linux   指定路径写法 2
'''

