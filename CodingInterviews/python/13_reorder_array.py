#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def reOrderArray(self, array):
        odd = []
        even = []
        for num in array:
            if num % 2 == 1:
                odd.append(num)
            else:
                even.append(num)

        return odd + even


if __name__ == "__main__":
    s = Solution()
    a = [2, 9, 19, 35, 34, 87, 96, 65]
    print(s.reOrderArray(a))
