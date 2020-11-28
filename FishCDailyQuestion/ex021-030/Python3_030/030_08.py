#!/usr/bin/env python3
# coding:utf-8

from random import randrange


def result(r, h):
    guess = ["石头", "剪刀", "布"]
    if r == h or guess[r] == guess[h]:
        print(f"双方均为：{guess[r]}，平手")
    elif r == h - 1:
        print(f"对方：{guess[r]}，我方：{guess[h]}\n你输了")
    else:
        print(f"对方：{guess[r]}，我方：{guess[h]}\n你赢了")
 

def rock_paper_scissors():
    human = input("0 石头，1 剪刀，2 布，q 退出：").strip()
    while human != 'q' and human != 'Q':
        try:
            human = int(human)
            if human not in [0, 1, 2]:
                raise ValueError
            robot = randrange(-1, 2)
            result(robot, human)
            human = input("\n0 石头，1 剪刀，2 布，q 退出：").strip()
        except ValueError:
            human = input("输入有误！请重输：").strip()


if __name__ == "__main__":
    rock_paper_scissors()
