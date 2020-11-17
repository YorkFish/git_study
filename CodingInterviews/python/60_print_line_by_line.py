# /usr/bin/env python3
# coding:utf-8

from helper import TreeNode


class Solution:
    def Print(self, pRoot):
        if pRoot is None:
            return []

        def getNodes(up, down):
            res = []
            while up:
                node = up.pop(0)
                res.append(node.val)
                if node.left:
                    down.append(node.left)
                if node.right:
                    down.append(node.right)
            return res

        queue1 = [pRoot]
        queue2 = []
        res = []
        while queue1 or queue2:
            if queue1:
                res.append(getNodes(queue1, queue2))
            if queue2:
                res.append(getNodes(queue2, queue1))
        return res


if __name__ == "__main__":
    """
         0
       /   \
      1     2
     / \   /
    3   4 5
    """
    n0 = TreeNode(0)
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n0.left = n1
    n0.right = n2
    n1.left = n3
    n1.right = n4
    n2.left = n5

    s = Solution()
    print(s.Print(n0))
