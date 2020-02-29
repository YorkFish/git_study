#!/usr/bin/env python3
# coding:utf-8

import random as r


def rock_paper_scissors():
    guess = ["石头", "剪刀", "布", "石头"]
    human = input(f"{guess[:3]}：")
    while human != 'q' and human != 'Q':
        try:
            if human not in guess:
                raise
            robot = r.choice(guess[:3])
            if human == robot:
                print("Draw")
            elif robot == guess[guess.index(human) + 1]:
                print(f"robot: {robot}, you win")
            else:
                print(f"robot: {robot}, you lost")
            human = input(f"\n{guess[:3]}：")
        except:
            human = input(f"输入有误！{guess[:3]}：")


if __name__ == "__main__":
    rock_paper_scissors()
