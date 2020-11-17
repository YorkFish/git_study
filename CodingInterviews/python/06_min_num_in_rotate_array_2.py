#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        """
        array1 = [4, 5, 1, 2, 3]
        array2 = [5, 1, 2, 3, 4]
        array3 = [3, 4, 5, 1, 2]
        """
        if rotateArray == []:
            return 0

        left = 0
        right = len(rotateArray) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if rotateArray[mid] < rotateArray[mid - 1]:
                return rotateArray[mid]
            elif rotateArray[mid] < rotateArray[right]:
                right = mid - 1
            else:
                left = mid + 1
        return rotateArray[0]


if __name__ == "__main__":
    ra = [3, 4, 5, 6, 1, 2]
    # ra = [1, 1, 1]

    s = Solution()
    ans = s.minNumberInRotateArray(ra)
    print(ans)
