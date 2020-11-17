#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def maxInWindows(self, num, size):
        if num == []:
            return []
        if len(num) < size:
            return [max(num)]

        res = []
        queue = num[:size]
        res.append(max(queue))
        for i in range(size, len(num)):
            queue.pop(0)
            queue.append(num[i])
            res.append(max(queue))
        return res


if __name__ == "__main__":
    nums = [2, 3, 4, 2, 6, 2, 5, 1]
    size = 3

    s = Solution()
    ans = s.maxInWindows(nums, size)
    print(ans)
