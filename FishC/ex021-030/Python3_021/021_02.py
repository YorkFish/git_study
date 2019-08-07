#!/usr/bin/env python3
# coding:utf-8

import os

def arrange(addr):
    """
    前提：文件夹中全是满足条件的图片
    功能：生成指定的文件夹；将图片放入对应的文件夹
    addr:   指定的目录
    return: 输出一个收集 jpg 文件信息的 list
    """
    os.chdir(addr)
    jpg_set = set()
    jpg_list = list()
    for afile in os.listdir():
        jpg_set.add(afile.split('-')[0])
        jpg_list.append(afile)

    for each in jpg_set:
        os.mkdir(each)

    for jpg in jpg_list:
        name = jpg.split('-')[0]
        if name in jpg_set:
            os.system(f"move ./{jpg} ./{name}") # 会在控制台输出“移动了         1 个文件。”

    return None


# 开始工作
# dir1 = input("请输入目标文件夹地址: ")
arrange("d:\\Filetest")


# 知识点
# os.getcwd() # 当前目录
# os.curdir # 返回一个 '.'，表示当前地址
# os.listdir() # 默认将当前地址的所有文件打包成列表返回（仅一层），括号中可以指定地址
# os.path.isfile(afile) # 若 afile 是文件夹，则返回 True
# os.path.splitext(afile) # 分离 afile 的文件名与扩展名，返回一个元组
