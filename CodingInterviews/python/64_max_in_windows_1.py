#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def maxInWindows(self, num, size):
        if num == []:
            return []
        if len(num) < size:
            return [max(num)]

        res = []
        for i in range(len(num) - size + 1):
            res.append(max(num[i:i + size]))
        return res


if __name__ == "__main__":
    nums = [2, 3, 4, 2, 6, 2, 5, 1]
    size = 3

    s = Solution()
    ans = s.maxInWindows(nums, size)
    print(ans)
