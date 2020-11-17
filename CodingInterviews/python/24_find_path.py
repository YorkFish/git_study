#!/usr/bin/env python3
# coding:utf-8

from helper import TreeNode


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if root is None:
            return []

        res = []
        route = [root]
        routes = [[root.val]]
        while route:
            node = route.pop(0)
            tempRoute = routes.pop(0)
            if (node.left is None and node.right is None
                    and sum(tempRoute) == expectNumber):
                res.insert(0, tempRoute)  # 我觉得不是字典序
                continue
            if node.left:
                route.append(node.left)
                temp = tempRoute[:]
                temp.append(node.left.val)
                routes.append(temp)
            if node.right:
                route.append(node.right)
                temp = tempRoute[:]
                temp.append(node.right.val)
                routes.append(temp)
        return res


if __name__ == "__main__":
    """
        1
       / \
      2   3
       \   \
        5   4
    """
    root = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    root.left = t2
    root.right = t3
    t2.right = t5
    t3.left = t4

    s = Solution()
    print(s.FindPath(root, 8))
    print(s.FindPath(root, 9))
