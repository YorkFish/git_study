#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if rotateArray == []:
            return 0

        for i in range(len(rotateArray) - 1):
            if rotateArray[i + 1] < rotateArray[i]:
                return rotateArray[i + 1]
        return rotateArray[0]


if __name__ == "__main__":
    # ra = [3, 4, 5, 6, 1, 2]
    ra = [2, 2, 3, 4, 5, 1, 2]

    s = Solution()
    ans = s.minNumberInRotateArray(ra)
    print(ans)
