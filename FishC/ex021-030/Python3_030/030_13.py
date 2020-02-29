#!/usr/bin/env python3
# coding:utf-8

from random import choice


def rock_paper_scissors():
    guess = ["石头", "剪刀", "布"]
    rules = [["布", "石头"], ["石头", "剪刀"], ["剪刀","布"]]
    while True:
        human = input("\n0 石头，1 剪刀，2 布，q 退出：").strip()
        if human == 'q' or human == 'Q':
            break
        elif human not in ['0', '1', '2']:
            print("输入有误，请重输")
            continue
        human = guess[eval(human)]
        robot = choice(guess)
        if robot == human:
            print("平")
        elif [robot, human] in rules:
            print("败")
        else:
            print("胜")


if __name__ == "__main__":
    rock_paper_scissors()
