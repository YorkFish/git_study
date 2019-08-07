#!/usr/bin/env python3
# coding:utf-8

import os, shutil

def fun(addr):
    items = os.listdir(addr)
    for each in items:
        if os.path.isfile(each):                        # 是文件，返回 True；是目录，返回 False
            item = os.path.splitext(each)[0]
            name = item.split("-")[0]                   # 文件名分割，获取 - 前面的内容
            if os.path.exists(addr + '/' + name):       # 去新路径下判断有没有以这个名字命名的文件夹
                shutil.move(each, addr + '/' + name)    # 如果存在就将文件移动到这个文件夹内
            else:                                       # 如果不存在就新建一个文件夹，并将文件存入
                os.mkdir(addr + '/' + name)
                shutil.move(each, addr + '/' + name)
        else:
            fun(each)                                   # 如果是目录的话回调函数

def arrange(addr):
    os.chdir(addr)
    for each in os.listdir(addr):
        if os.path.isfile(each):            # 是文件，返回 True；是目录，返回 False
            name = each.split("-")[0]       # 获取文件名
            if not os.path.exists(name):    # 去新路径下判断有没有以这个名字命名的文件夹
                os.mkdir(name)
            shutil.move(each, name)         # 如果存在就将文件移动到这个文件夹内

arrange("D:/Filetest")
