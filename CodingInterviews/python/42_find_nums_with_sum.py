#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        left = 0
        right = len(array) - 1
        while left < right:
            twoSum = array[left] + array[right]
            if twoSum == tsum:
                return [array[left], array[right]]
            elif twoSum < tsum:
                left += 1
            else:
                right -= 1
        return []


if __name__ == "__main__":
    array = [2, 3, 4, 5, 6, 7, 8, 9]
    tsum = 9

    s = Solution()
    ans = s.FindNumbersWithSum(array, tsum)
    print(ans)
