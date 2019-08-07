#!/usr/bin/env python3
# coding:utf-8

import os, shutil

curdir = "D:\\Filetest"
os.chdir(curdir)

file_names = []
for file in os.listdir():
    if file.endswith('.jpg'):
        file_names.append(file)

for file_name in file_names:
    prefix = file_name.split('-')[0]
    if not os.path.isdir(os.path.join(curdir, prefix)):
        os.mkdir(prefix)
    shutil.move(os.path.join(curdir, file_name), os.path.join(curdir, prefix))

# 知识点
# os.path.isdir(addr) # 判断 addr 是否是文件夹
# file.endswith('.jpg') # 判断后缀是否是 ".jpg"
# os.path.join(curdir, prefix) # 以路径的形式将 prefix 加至 curdir 之后
# os.path.join(addr1, addr2, addr3, ...) # 路径可以叠加
