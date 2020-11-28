#!/usr/bin/env python3
# coding:utf-8

def get_num(n):
    num_dict = {}
    for i in range(1, n+1):
        num_dict[i] = i							# {编号（不动）:元素（表示状态）}
    
    # 记下方 for 循环为 (1)
    for j in range(n-3, 0, -1):					# 配合 17 行的 +j
        for x in num_dict:
            if num_dict[x] >= 3:				# 除去 3 的倍数
                num_dict[x] -= 3
            elif num_dict[x] == 0:				# 已经退出的数字
                pass
            else:								# num_dict[x] 等于 1 或 2
                num_dict[x] += j				# (2)

    for k in num_dict.keys():
        if num_dict[k] == 2:					# 无论剩下 1，2，还是 1，2，3，必是 2 取胜
            print("\nThe lucky number is: {}".format(k))
'''
(1) 可以这样理解：
    n > 3 时进入循环
    循环前共 n 个数，循环后剩 3 个数，且为 1，2，3
    每次循环少一个数，即循环了 n-3 次

(2) 可以这样理解：
    一来是为了循环
    二来是顺应规律（这个规律有些抽象）
        数字为 1 或 2 时,第 1 次循环 +(n-3)，第 2 次 +(n-4)，直到第 n-3 次 +1

举个例子
    {1:1, 2:2, 3:3, 4:4, 5:5} —— n-3=2，所以循环 2 轮
=>  {1:3, 2:4, 3:0, 4:1, 5:2} —— 第 1 轮，j=2，所以元素为 1 或 2 的 +2，没有为 0 的，其他 -3
=>  {1:0, 2:1, 3:0, 4:2, 5:3} —— 第 2 轮，j=1，所以元素为 1 或 2 的 +1，为 0 的不变，其他 -3
循环结束，元素 2 对应的编号为 4，所以 4 胜出
'''

def run():
    num = int(input("Please enter the number of people: "))
    if num == 1:
        print("\nYou can't play alone.")
    elif num > 1:
        get_num(num)
    else:
        print("Please enter a natural number greater than 0.")

if __name__ == '__main__':
    run()

