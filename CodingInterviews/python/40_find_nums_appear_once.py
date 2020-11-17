#!/usr/bin/env python3
# coding:utf-8


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if array == [] or len(array) % 2 == 1:
            return None

        axorb = array[0]
        for i in range(1, len(array)):
            axorb ^= array[i]
        mask = 1  # mask 可以区分两个单独的数，其他的数会成双地“站队”并消掉
        while axorb % 2 == 0:
            axorb >>= 1
            mask <<= 1
        teamA = None
        teamB = None
        for num in array:
            if num & mask == 0:
                if teamA is None:
                    teamA = num
                else:
                    teamA ^= num
            else:
                if teamB is None:
                    teamB = num
                else:
                    teamB ^= num
        return teamA, teamB


if __name__ == "__main__":
    array = [1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 7]

    s = Solution()
    num1, num2 = s.FindNumsAppearOnce(array)
    print(num1, num2)
