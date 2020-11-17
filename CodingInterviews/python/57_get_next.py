# /usr/bin/env python3
# coding:utf-8

from helper import BinaryTreeTraverse, TreeLinkNode


class Solution(object):
    def getNext(self, pNode):
        """
        寻找右子树
        1. 若存在，就一直找到该右子树的最左边
        2. 不存在，就向上寻找父结点，一直找到某结点是其父结点的左子树，打印此父结点
        """
        if pNode.right:
            tmp = pNode.right
            while tmp.left:
                tmp = tmp.left
            return tmp
        else:
            tmp = pNode
            while tmp.next:
                if tmp.next.left is tmp:
                    return tmp.next
                tmp = tmp.next
            return None


if __name__ == "__main__":
    """
        next              0
         ^              /   \
        node      =>   1     2
        /  \          / \   /
    left   right     3   4 5
    """
    n0 = TreeLinkNode(0)
    n1 = TreeLinkNode(1)
    n2 = TreeLinkNode(2)
    n3 = TreeLinkNode(3)
    n4 = TreeLinkNode(4)
    n5 = TreeLinkNode(5)
    n0.left = n1
    n0.right = n2
    n1.next = n0
    n1.left = n3
    n1.right = n4
    n2.next = n0
    n2.left = n5
    n3.next = n1
    n4.next = n1
    n5.next = n2

    b = BinaryTreeTraverse()
    print("mid order traverse:")
    b.mid_order(n0)
    print()

    s = Solution()
    print(f">>> node0's next: {s.getNext(n0).val}")
    print(f">>> node1's next: {s.getNext(n1).val}")
    print(f">>> node1's next: {s.getNext(n2)}")
    print(f">>> node3's next: {s.getNext(n3).val}")
    print(f">>> node4's next: {s.getNext(n4).val}")
