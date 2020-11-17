#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if array == []:
            return None

        res = array[0]
        tmp = array[0]
        for i in range(1, len(array)):
            if tmp < 0:
                tmp = array[i]
            else:
                tmp += array[i]
            if res < tmp:
                res = tmp
        return res


if __name__ == "__main__":
    array = [-2, -8, -1, -5, -9]

    s = Solution()
    ans = s.FindGreatestSumOfSubArray(array)
    print(ans)
