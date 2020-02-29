#!/usr/bin/env python3
# coding:utf-8

"""
借助前方高手的代码
robot - human, human - robot 都行
就是将 平-胜-负 由 if-elif-else 转化为列表与索引
"""

from random import randrange


def rock_paper_scissors():
    rps = ["石头", "剪刀", "布"]
    res = ["平局", "你赢了", "你输了"]
    while True:
        human = input("\n0 石头，1 剪刀，2 布，q 退出：").strip()
        if human == 'q' or human == 'Q':
            break
        if human not in ['0', '1', '2']:
            print("输入有误，请按规则重输")
            continue
        r = randrange(0, 3)
        h = eval(human)
        print(f"对方：{rps[r]}，我方：{rps[h]}，{res[r-h]}")


if __name__ == "__main__":
    rock_paper_scissors()
