#!/usr/bin/env python3
# coding:utf-8

from helper import PrintTree, TreeNode
from helper import print_deque, print_linked_list


class Solution:
    def Convert(self, pRootOfTree):
        if pRootOfTree is None:
            return None

        leftNode = self.Convert(pRootOfTree.left)
        rightNode = self.Convert(pRootOfTree.right)
        if leftNode:
            res = leftNode
            while leftNode.right:
                leftNode = leftNode.right
        else:
            res = pRootOfTree

        pRootOfTree.left = leftNode
        pRootOfTree.right = rightNode

        if leftNode:
            leftNode.right = pRootOfTree
        if rightNode:
            rightNode.left = pRootOfTree
        return res


if __name__ == "__main__":
    """
         4
       /   \
      2     6    =>  1 <=> 2 <=> 3 <=> 4 <=> 5 <=> 6 <=> 7
     / \   / \
    1   3 5   7
    """
    root = TreeNode(4)
    b1 = TreeNode(2)
    b2 = TreeNode(6)
    b3 = TreeNode(1)
    b4 = TreeNode(3)
    b5 = TreeNode(5)
    b6 = TreeNode(7)
    root.left = b1
    root.right = b2
    b1.left = b3
    b1.right = b4
    b2.left = b5
    b2.right = b6

    p = PrintTree()
    p.from_top_to_bottom(root)

    s = Solution()
    ans = s.Convert(root)

    leftNode = ans
    while ans.right:
        ans = ans.right
    rightNode = ans
    print_deque(leftNode, rightNode)
