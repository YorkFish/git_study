#!/usr/bin/env python3
# coding:utf-8

from random import choice


def rock_paper_scissors():
    R = {'石头': 1, '剪刀': 2, '布': 3}
    H = {'石头': 2, '剪刀': 3, '布': 1}
    while True:
        robot = choice(['石头', '剪刀', '布'])
        human = input("石头、剪刀、布：")
        print(f"对方；{robot}，我方：{human}")
        if R[robot] == H[human]:
            print("你赢了")
            break
        elif robot == human:
            print("平局")
        else:
            print("你输了")


if __name__ == "__main__":
    rock_paper_scissors()
