#!/usr/bin/env python3
# coding:utf-8

"""
平手以外的情况
human  robot  human-robot  human
    0  2      -2           win
    0  5      -5
    2  0       2
    2  5      -3           win
    5  0       5           win
    5  2       3
"""

from random import choice


def rock_paper_scissors():
    rps_d = {0:"石头", 2:"剪刀", 5:"布"}
    rps_l = [0, 2, 5]
    robot = choice(rps_l)
    human = int(input("请输入手势代号（0 石头，2 剪刀，5 布）："))
    while human not in rps_l:
        human = int(input("输入有误，请重输："))

    if human == robot:
        print(f"双方均为：{rps_d[human]}，平手")
        return

    print(f"我方：{rps_d[human]}，对方：{rps_d[robot]}，", end='')
    if human - robot in [-2, -3, 5]:
        print("你赢了")
    else:
        print("你输了")
    return


if __name__ == "__main__":
    rock_paper_scissors()
