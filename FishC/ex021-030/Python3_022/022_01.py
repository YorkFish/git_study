#!/usr/bin/env python3
# coding:utf-8

# 改进小红球
class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts) # 打乱 starts
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height() # 获取高度坐标
        self.canvas_width = self.canvas.winfo_width() # 获取宽度坐标

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id) # 获取坐标
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

# 把小球加入主循环
while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

