#!/usr/bin/env python3
# coding:utf-8

from helper import TreeNode


class Solution:
    def isSymmetrical(self, pRoot):
        def judgeSym(nodeL, nodeR):
            if nodeL is None and nodeR is None:
                return True
            elif nodeL is None or nodeR is None:
                return False
            elif nodeL.val != nodeR.val:
                return False
            else:
                return judgeSym(nodeL.left, nodeR.right) and\
                        judgeSym(nodeL.right, nodeR.left)

        if pRoot is None:
            return True
        return judgeSym(pRoot.left, pRoot.right)


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

    """
        0
       / \
      1   1
     /   /
    2   2
    """
    t0 = TreeNode(0)
    t1 = TreeNode(1)
    t2 = TreeNode(1)
    t3 = TreeNode(2)
    t5 = TreeNode(2)
    t0.left = t1
    t0.right = t2
    t1.left = t3
    t2.left = t5

    s = Solution()
    print(s.isSymmetrical(n0))
    print(s.isSymmetrical(t0))
