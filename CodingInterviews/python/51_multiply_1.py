#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def multiply(self, A):
        n = len(A)
        left = [1] * n
        right = [1] * n
        B = [0] * n
        
        for i in range(n-1):
            left[i+1] = left[i] * A[i]
            right[n-2-i] = right[n-1-i] * A[n-1-i]
        for i in range(n):
            B[i] = left[i] * right[i]
        
        return B


if __name__ == "__main__":
    array = [1, 2, 3, 4]

    s = Solution()
    ans = s.multiply(array)
    print(ans)
