# /usr/bin/env python3
# coding:utf-8

from helper import TreeNode
from helper import BinaryTreeTraverse


class Solution:
    def Serialize(self, root):
        def preOrder(root):
            """先序遍历，数字转字符串，None 转 #"""
            if root is None:
                resList.append('#')
                return

            resList.append(str(root.val))
            preOrder(root.left)
            preOrder(root.right)

        resList = []
        preOrder(root)
        return ' '.join(resList)

    def Deserialize(self, s):
        def dePreOrder():
            if resList == []:
                return None

            rootVal = resList.pop(0)
            if rootVal == '#':
                return None

            node = TreeNode(int(rootVal))
            nodeL = dePreOrder()
            nodeR = dePreOrder()
            node.left = nodeL
            node.right = nodeR
            return node

        resList = s.split()
        return dePreOrder()


if __name__ == "__main__":
    """
         1
       /   \
      2     5
     / \   /
    3   4 6
    """
    n0 = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(5)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(6)
    n0.left = n1
    n0.right = n2
    n1.left = n3
    n1.right = n4
    n2.left = n5

    s = Solution()
    serialize = s.Serialize(n0)
    print(f"serialize = {serialize}")

    root = s.Deserialize(serialize)
    b = BinaryTreeTraverse()
    b.pre_order(root)
