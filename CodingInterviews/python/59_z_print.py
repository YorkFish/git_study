# /usr/bin/env python3
# coding:utf-8

from helper import TreeNode


class Solution:
    """
       > -
          v
     - < -
    v
     - >
    """
    def Print(self, pRoot):
        if pRoot is None:
            return []

        stack1 = [pRoot]
        stack2 = []
        res = []
        while stack1 or stack2:
            if stack1:
                tmpRes = []
                while stack1:
                    tmpNode = stack1.pop()
                    tmpRes.append(tmpNode.val)
                    if tmpNode.left:
                        stack2.append(tmpNode.left)
                    if tmpNode.right:
                        stack2.append(tmpNode.right)
                res.append(tmpRes)
            if stack2:
                tmpRes = []
                while stack2:
                    tmpNode = stack2.pop()
                    tmpRes.append(tmpNode.val)
                    if tmpNode.right:
                        stack1.append(tmpNode.right)
                    if tmpNode.left:
                        stack1.append(tmpNode.left)
                res.append(tmpRes)
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
    print(s.Print(None))
    print(s.Print(n0))
