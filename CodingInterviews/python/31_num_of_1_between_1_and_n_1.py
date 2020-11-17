#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        if n < 1:
            return 0

        head = mid = tail = 1
        val = 1
        res = 0
        while head != 0:
            head = n // val // 10
            mid = n // val % 10
            tail = n % val
            if mid == 0:  # 123(0)5 -> 0~122
                increment = head * val  # tail 多一位，head 多乘 10
            elif mid > 1:  # 123(4)5 -> 0~123
                increment = (head + 1) * val
            else:  # 123(1)5 -> 0~12300, 12300~12315 -> 0~122, 0~5
                increment = head * val + tail + 1
            print(head, mid, tail, increment)
            res += increment
            val *= 10
        return res


if __name__ == "__main__":
    n = 200

    s = Solution()
    ans = s.NumberOf1Between1AndN_Solution(n)
    print(ans)
