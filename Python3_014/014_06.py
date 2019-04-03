#!/usr/bin/env python3
# coding:utf-8

'''
# 列出参与人数少于等于 20 时的获胜编号
num_list = [0, 1]	# 0 是占位，方便下标与编号对应

for num in range(2, 21):
    num_list.append((num_list[num-1] + 2) % num + 1)

for i, j in enumerate(num_list):
    print(i, j)
'''

'''
用上方代码得到下面数据：
|参与人数|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|
|获胜编号|1|2|2|1|4|1|4|7|1| 4| 7|10|13| 2| 5| 8|11|14|17|20|

规律：
    下一个获胜编号为上一个获胜编号 +3，如
        参与人数为 6 时，获胜编号为 1，则
        参与人数为 7 时，获胜编号为 1+3 = 4
    如果超过人数的值，则减去人数，如
        参与人数为 13 时，获胜编号为 13，则
        参与人数为 14 时，获胜编号为 (13+3)-14 = 2 （因为循环）
'''

def get_num(n):
    num = 1
    for i in range(2, n+1):
        num += 3
        if num > i:
            num -= i

    return num

if __name__ == '__main__':
    num = int(input("Please enter the number of people: "))
    print("\nThe lucky number is:", get_num(num))

