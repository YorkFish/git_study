#!/usr/bin/env python3
# coding:utf-8

from random import randrange


def rock_paper_scissors():
    rps = {1: "石头", 2: "剪刀", 3: "布", 4: "石头"}
    human = int(input("1 石头，2 剪刀，3 布："))
    robot = randrange(1, 4)
    if robot == human:
        print('平')
    elif rps[robot] == rps[human+1]:
        print('胜')
    else:
        print('负')


if __name__ == "__main__":
    rock_paper_scissors()
