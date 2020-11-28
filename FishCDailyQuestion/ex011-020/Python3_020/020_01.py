#!/usr/bin/env python3
# coding:utf-8

# 创建游戏画布
from tkinter import *
import random
import time

tk = Tk()                       # new 一个对象
tk.title("Ball Game")           # 将窗口命名为 Ball Game
tk.resizable(0,0)               # 使窗口不能被拉伸
tk.wm_attributes("-topmost", 1) # 置顶

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0) # 宽 500px，高 400px，边框宽度设为 0
canvas.pack()                   # 布局组件
tk.update()                     # 刷新窗口

# 创建 Ball 类
class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

    def draw(self):
        pass

# 创建主循环
while 1:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

# 创建实例化对象
ball = Ball(canvas, 'red')
