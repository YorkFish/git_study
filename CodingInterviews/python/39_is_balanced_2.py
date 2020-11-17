#!/usr/bin/env python3
# coding:utf-8

from helper import TreeNode


class Solution:
    def IsBalanced_Solution(self, pRoot):
        return self.dfs(pRoot) != -1

    def dfs(self, node):
        if node is None:
            return 0
        l = self.dfs(node.left)
        if l == -1:
            return -1
        r = self.dfs(node.right)
        if r == -1:
            return -1
        if abs(l - r) > 1:
            return -1
        return max(l, r) + 1


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
