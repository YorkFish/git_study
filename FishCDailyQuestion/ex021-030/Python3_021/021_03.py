#!/usr/bin/env python3
# coding:utf-8

import os, shutil

def new_path(path):
    os.chdir(path)
    file_dict = {}
    files = os.listdir()

    # 把 jpg 文件找出来，建字典区分文件名和数字串 
    for file in files:
        if file[-3:] == 'jpg':
            file_dict[file] = file.split('-')[0]
        else: pass

    # 新建文件夹，要防止文件夹已存在
    for each_value in file_dict.values():
        try:
            os.mkdir(each_value)
        except OSError: pass

    # 移动文件
    for each_key in file_dict.keys():
        shutil.move(each_key, file_dict[each_key])

def new_path2(addr):
    os.chdir(addr)
    file_dict = {}
 
    for file in os.listdir():               # 把 jpg 文件找出来，建字典区分文件名和数字串
        if file[-3:] == 'jpg':
            file_dict[file] = file.split('-')[0]
        else: pass

    for each_key, each_value in file_dict.items():
        try:                                # 新建文件夹，要防止文件夹已存在
            os.mkdir(each_value)
        except FileExistsError: pass

        shutil.move(each_key, each_value)   # 移动文件

new_path2("d:\\Filetest")
