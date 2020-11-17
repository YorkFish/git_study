#!/usr/bin/env python3
# coding:utf-8

from helper import TreeNode


class Solution:
    def isSymmetrical(self, pRoot):
        if pRoot is None:
            return True

        stack = []
        stack.extend([pRoot.right, pRoot.left])
        while stack:
            nodeL = stack.pop()
            nodeR = stack.pop()
            if nodeL is None and nodeR is None:
                continue
            elif nodeL is None or nodeR is None:
                return False
            elif nodeL.val != nodeR.val:
                return False
            stack.extend([nodeR.right, nodeL.left, nodeR.left, nodeL.right])
        return True


if __name__ == "__main__":
    """
         1
       /   \
      2     2
     / \   / \
    3   4 4   3
    """
    n0 = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(4)
    n6 = TreeNode(3)
    n0.left = n1
    n0.right = n2
    n1.left = n3
    n1.right = n4
    n2.left = n5
    n2.right = n6

    s = Solution()
    print(s.isSymmetrical(n0))
