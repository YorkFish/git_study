#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def GetNumberOfK(self, data, k):
        if data == [] or k > data[-1]:
            return 0

        left = 0
        right = len(data) - 1
        while left < right:
            mid = left + (right - left) // 2
            if data[mid] < k:
                left = mid + 1
            else:
                right = mid
        if data[left] != k:
            return 0
        while left - 1 > 0 and data[left - 1] == k:
            left -= 1
        while right + 1 < len(data) and data[right + 1] == k:
            right += 1
        return right - left + 1


if __name__ == "__main__":
    data = [1, 3, 3, 3, 3, 4, 5]
    # k = 2
    # k = 3
    # k = 4
    k = 6

    s = Solution()
    ans = s.GetNumberOfK(data, k)
    print(ans)
