#!/usr/bin/env python3
# coding:utf-8

# 桃子数累加；分桃顺着分
def peach_calc(peaches):
    monkeys = 0
    tmp = peaches
    while (tmp - 1) % 5 == 0:
        tmp = (tmp - 1) /5 *4
        monkeys += 1
        if monkeys == 5:	# 成功地分了 5 次
            return peaches
    return False

def run():
    peaches = 6				# 第 5 只猴子分之前至少有 6 只桃子
    while True:
        tale = peach_calc(peaches)
        if tale:
            print("Sum =", tale)
            break
        else :
            peaches += 5	# 5 只猴子，每只每次 +1，故每次总共 +5

if __name__ == '__main__':
    run()

