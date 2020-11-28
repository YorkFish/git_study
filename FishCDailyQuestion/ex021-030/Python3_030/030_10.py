#!/usr/bin/env python3
#coding:utf-8

from random import randrange


def rock_paper_scissors():
    rps = ["石头", "剪刀", "布"]
    while True:
        human = input("\n0 石头，1 剪刀，2 布，q 退出：").strip()
        if human == 'q' or human == 'Q':
            break
        if human not in ['0', '1', '2']:
            print("输入有误，请按规则重输")
            continue
        human = eval(human)
        robot = randrange(0, 3)
        if robot == human:
            print("draw")
        elif (robot, human) == (0, 2)\
                or (robot, human) == (1, 0)\
                or (robot, human) == (2, 1):
            print(f"对方：{rps[robot]}，你赢了")
        else:
            print(f"对方：{rps[robot]}，你输了")


if __name__ == "__main__":
    rock_paper_scissors()
