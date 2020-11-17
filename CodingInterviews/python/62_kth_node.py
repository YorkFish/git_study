# /usr/bin/env python3
# coding:utf-8

from helper import TreeNode


class Solution:
    def KthNode(self, pRoot, k):
        def midOrder(pRoot):
            if pRoot is None:
                return None
            midOrder(pRoot.left)
            res.append(pRoot)
            midOrder(pRoot.right)

        res = []
        midOrder(pRoot)
        if len(res) < k or k < 1:
            return None
        return res[k - 1]


if __name__ == "__main__":
    """
          8
       /    \
      6     10
     / \   /  \
    5   7 9   11
    """
    n0 = TreeNode(8)
    n1 = TreeNode(6)
    n2 = TreeNode(10)
    n3 = TreeNode(5)
    n4 = TreeNode(7)
    n5 = TreeNode(9)
    n6 = TreeNode(11)
    n0.left = n1
    n0.right = n2
    n1.left = n3
    n1.right = n4
    n2.left = n5
    n2.right = n6

    s = Solution()
    ans = s.KthNode(n0, 1)
    print(ans.val)
