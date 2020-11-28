#!/usr/bin/env python3
# coding:utf-8

from random import choice


def rock_paper_scissors():
    rps_d = {0:["石头", 5], 2:["剪刀", 0], 5:["布", 2]}  # 代号a:[名称, 克制a的代号b]
    rps_l = [0, 2, 5]
    robot = choice(rps_l)
    human = int(input("请输入手势代号（0 石头，2 剪刀，5 布）："))
    while human not in rps_l:
        human = int(input("输入有误，请重输："))

    if human == robot:
        print(f"双方均为：{rps_d[human][0]}，平手")
        return

    print(f"我方：{rps_d[human][0]}，对方：{rps_d[robot][0]}，", end='')
    if human == rps_d[robot][1]:
        print("你赢了")
    else:
        print("你输了")
    return


if __name__ == "__main__":
    rock_paper_scissors()
