#!/usr/bin/env pythn3
# coding:utf-8

""" 先定输赢，反推手势 """

from random import randint


def rock_paper_scissors():
    while True:
        human = input("\n1 锤，2 剪，3 布\n请输入数字：").strip()
        if human in ['1', '2', '3']:
            break
        print("输入错误，请重新输入")

    rps = ['锤', '剪', '布']
    human = eval(human)
    guess = randint(1, 3)
    if guess == 1:
        print(f"我方：{rps[human-1]}，对方：{rps[human-3]}，你赢了")
    elif guess == 2:
        print(f"我方：{rps[human-1]}，对方：{rps[human-2]}，你输了")
    else:
        print(f"双方均出：{rps[human-1]}，平局")


if __name__ == "__main__":
    rock_paper_scissors()
