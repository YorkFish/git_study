#!/usr/bin/env python3
# coding:utf-8

# 用递归倒推
def peach_calc(monkeys, peaches):
    if monkeys == 1:
        return peaches
    else:
        return peach_calc(monkeys-1, peaches) /4 *5 +1

def run():
    peaches = 6				# 第 5 只猴子分之前至少有 6 只桃子
    while True:
        tale = peach_calc(5, peaches)
        if tale % 1 == 0:
            print("Sum = %d" % tale)
            break
        else:
            peaches += 5	# 5 只猴子，每只每次 +1，故每次总共 +5

if __name__ == '__main__':
    run()

