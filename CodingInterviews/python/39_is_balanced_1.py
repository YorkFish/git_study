#!/usr/bin/env python3
# coding:utf-8

from helper import TreeNode


class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot is None:
            return True

        def getDepth(node):
            if node is None:
                return 0

            l = getDepth(node.left)
            r = getDepth(node.right)
            if abs(l - r) > 1:
                self.isBalance = False
            return max(l, r) + 1
        
        self.isBalance = True
        getDepth(pRoot)
        return self.isBalance


if __name__ == "__main__":
    """
        1
       / \
      2   3
     /
    4
    """
    root = TreeNode(0)
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    root.left = n1
    root.right = n2
    n1.left = n3

    s = Solution()
    ans = s.IsBalanced_Solution(root)
    print(ans)
