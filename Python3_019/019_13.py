#!/usr/bin/env python3
# coding:utf-8

# 只是引入“泡菜”而已，并不是新的思路
import os, pickle

def save_text(pf, text):
    '''保存文件'''
    with open(pf, 'wb') as f:
        pickle.dump(text, f)

def load_text(pf):
    '''载入文件'''
    with open(pf, 'rb') as f:
        text = pickle.load(f)
        print(text)

def run():
    p = "~/Desktop/"
    os.chdir(p)
    
    fn = input("请输入文件名，不必加后缀：")
    fn += ".txt"
    pf = p + fn
    
    if os.path.exists(fn):
        print("文件已经存在!")
        return		# 结束次函数
    
    text = []
    while True:
        one_line = input("请输入内容（单独输入“.”为结束）：")
        if one_line == ".":
            break
        text.append(one_line)
    save_text(pf, text)
    #load_text(pf)    

if __name__ == "__main__":
    run()

