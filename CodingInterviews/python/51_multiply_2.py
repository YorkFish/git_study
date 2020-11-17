#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def multiply(self, A):
        B = [1] * len(A)
        for i in range(len(A) - 2, -1, -1):  # B[0] ~ B[-2]
            B[i] = B[i + 1] * A[i + 1]
        left = A[0]
        for i in range(1, len(A)):
            B[i] *= left
            left *= A[i]
        return B


if __name__ == "__main__":
    array = [1, 2, 3, 4]

    s = Solution()
    ans = s.multiply(array)
    print(ans)
