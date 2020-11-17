#!/usr/bin/env python3
# coding:utf-8

from helper import TreeNode


class Solution:
    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0

        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1


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
    ans = s.TreeDepth(root)
    print(ans)
