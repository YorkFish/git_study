#!/usr/bin/env python3
# coding:utf-8

import os, os.path, shutil

os.chdir("D:/Filetest")
for each in os.listdir():                           # os.listdir() 返回当前路径（可指定）下的文件和文件夹列表
    if os.path.isfile(each):                        # os.path.isfile(path) 判断 path 是否为文件
        path = each.split('-')[0]                   # 这里藏有 Bug，因为不符合 num1-num2.jpg 的文件名会原样赋给 path
        if not os.path.exists(path):                # os.path.exists(path) 路径存在就返回 True，否则返回 False
            os.mkdir(path)                          # 创建目录
        shutil.move(each, './' + path + '/' + each) # 移动或重命名
