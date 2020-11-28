"""
说一下我的思路，使用穷举法，但做些优化。
1. [1][1]位置肯定是5。
2. 每行列对角线之后是15
所以将1~9除了5以外排列出4个，将其填到[0][0],[0][1],[0][2],[1][0]位置，将10减去这个数排在相对的位置，如[0][0]填1，则[2][2]填9，当然这4个数要去除相互直接的和为10的。
再判断[0][0],[0][1][0][2]之和为15且[0][0],[1][0],[2][0]之和为15就可得到答案了。
这里为了方便没有采用二维列表，只用以为列表代替了。
"""

import itertools
count = 1
for i in itertools.permutations((1, 2, 3, 4, 6 , 7, 8, 9), 4):
    list1 = [0] * 9
    list1[4] = 5
    if len(set([10 - n for n in i]) & set(i)) == 0:
        for j in range(4):
            list1[j] = i[j]
        for j in range(4):
            list1[8 - j] = 10 - i[j]
        if list1[0] + list1[1] + list1[2] == 15 and list1[0] + list1[3] + list1[6] == 15:
            print('No.%d'%count)
            for m in range(3):
                print(list1[m * 3: (m + 1) * 3])
            print()
            count += 1
