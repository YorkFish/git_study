#!/usr/bin/env python3
# coding:utf-8

from helper import TreeNode


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 is None or pRoot2 is None:
            return False

        def isEqual(r1, r2):
            if r2 is None:  # r1 下面比 r2 多的部分可以不管
                return True
            elif r1 is None:
                return False
            elif r1.val != r2.val:
                return False
            return isEqual(r1.left, r2.left) and isEqual(r1.right, r2.right)

        return (isEqual(pRoot1, pRoot2) or isEqual(pRoot1.left, pRoot2) or
                isEqual(pRoot1.right, pRoot2))


if __name__ == "__main__":
    a1 = TreeNode(8)
    a2 = TreeNode(8)
    a3 = TreeNode(9)
    a4 = TreeNode(2)
    a5 = TreeNode(5)
    a1.left = a2
    a2.left = a3
    a3.left = a4
    a4.left = a5

    b1 = TreeNode(8)
    b2 = TreeNode(9)
    b3 = TreeNode(2)
    b1.left = b2
    b2.left = b3

    s = Solution()
    ans = s.HasSubtree(a1, a2)
    print(ans)
