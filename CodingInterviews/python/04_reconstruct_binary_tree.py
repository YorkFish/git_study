#!/usr/bin/env python3
# coding:utf-8

from helper import TreeNode
from helper import BinaryTreeTraverse


class Solution(object):
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if pre == [] or tin == [] or len(pre) != len(tin):
            return None

        root = TreeNode(pre[0])
        pos = tin.index(pre[0])

        root.left = self.reConstructBinaryTree(pre[1:pos+1], tin[:pos])
        root.right = self.reConstructBinaryTree(pre[pos+1:],  tin[pos+1:])
        return root


if __name__ == "__main__":
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]

    s = Solution()
    ans = s.reConstructBinaryTree(pre, tin)

    b = BinaryTreeTraverse()
    b.pre_order(ans)
    print('=' * 10)
    b.mid_order(ans)
