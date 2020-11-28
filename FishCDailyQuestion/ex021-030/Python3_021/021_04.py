#!/usr/bin/env python3
# coding:utf-8

import os, shutil

os.chdir(r"D:\Filetest")
dir_dict = dict()

for each in os.listdir():
    each_file = os.path.splitext(each)[0]               # 去掉扩展名，只留文件名
    each_file_id = each_file[:each_file.index('-')]     # 去掉文件名中-以及后面的字符
    dir_dict.setdefault(each, each_file_id)

for each_file, each_id in dir_dict.items():             # 依次创建文件夹
    if not os.path.exists(each_id):                     # 文件夹不存在即创建
        os.mkdir(each_id)
    shutil.move(each_file, "./"+each_id+'/'+each_file)  # 依次将文件 move 到对应文件夹
