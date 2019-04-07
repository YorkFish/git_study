#!/usr/bin/env python3
# coding:utf-8

# while + string
text = ""
while True:
    c = input("请输入一个数字（按 q 键退出)： ")
    if c == 'q' or c == 'Q':
        break
    else:
        text = c + ' ' + text
print(text)

