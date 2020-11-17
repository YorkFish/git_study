#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def IsPopOrder(self, pushV, popV):
        if pushV is None or len(pushV) != len(popV):
            return None

        stk = []
        idx = 0
        for num in pushV:
            stk.append(num)
            while stk and stk[-1] == popV[idx]:
                stk.pop()
                idx += 1
        return idx == len(popV)


if __name__ == "__main__":
    pushV = [1, 2, 3, 4, 5]
    popV1 = [4, 5, 3, 2, 1]
    popV2 = [4, 3, 5, 1, 2]

    s = Solution()
    print(s.IsPopOrder(pushV, popV1))
    print(s.IsPopOrder(pushV, popV2))
