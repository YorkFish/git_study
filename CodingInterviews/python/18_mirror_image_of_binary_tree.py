#!/usr/bin/env python3
# coding:utf-8

from helper import TreeNode
from helper import PrintTree


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root is None:
            return None
        
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root


if __name__ == "__main__":
    root = TreeNode(8)
    n1 = TreeNode(6)
    n2 = TreeNode(10)
    n3 = TreeNode(5)
    n4 = TreeNode(7)
    n5 = TreeNode(9)
    n6 = TreeNode(11)
    root.left = n1
    root.right = n2
    n1.left = n3
    n1.right = n4
    n2.left = n5
    n2.right = n6
    p = PrintTree()
    p.from_top_to_bottom(root)

    s = Solution()
    ans = s.Mirror(root)
    p.from_top_to_bottom(ans)
