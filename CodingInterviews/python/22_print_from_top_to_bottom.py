#!/usr/bin/env python3
# coding:utf-8

from helper import TreeNode


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if root is None or root == []:
            return []

        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(3)
    n3 = TreeNode(4)
    n4 = TreeNode(5)
    root.left = n1
    root.right = n2
    n1.left = n3
    n1.right = n4

    s = Solution()
    ans = s.PrintFromTopToBottom(root)
    print(ans)
