#!/usr/bin/env python3
# coding:utf-8

from random import randrange


def rock_paper_scissors():
    rps = ['', "石头", "剪刀", "布"]
    while True:
        human = input("\n1 石头，2 剪刀，3 布，q 退出：").strip()
        if human == 'q' or human == 'Q':
            break
        if human not in ['1', '2', '3']:
            print("输入有误，请重输")
            continue
        human = eval(human)
        robot = randrange(1, 4)
        if robot == human:
            print(f"双方：{rps[robot]}，平局")
        elif robot - human == 1 or robot - human == -2:
            print(f"对方：{rps[robot]}，我方：{rps[human]}，你赢了！")
        else:
            print(f"对方：{rps[robot]}，我方：{rps[human]}，你输了！")


if __name__ == "__main__":
    rock_paper_scissors()
