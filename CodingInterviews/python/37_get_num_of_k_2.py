#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def GetNumberOfK(self, data, k):
        if data == [] or k > data[-1]:
            return 0

        def binSearch(data, num):
            left = 0
            right = len(data) - 1
            while left < right:
                mid = left + (right - left) // 2
                if data[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            return left

        if data[-1] == k:
            stop = len(data)
        else:
            stop = binSearch(data, k + 0.5)
        return stop - binSearch(data, k - 0.5)


if __name__ == "__main__":
    # data = [1, 3, 3, 3, 3, 4, 5]
    # k = 2
    # k = 3
    # k = 4
    # k = 6

    data = [1, 2, 3, 3, 3, 3]
    k = 3

    s = Solution()
    ans = s.GetNumberOfK(data, k)
    print(ans)
