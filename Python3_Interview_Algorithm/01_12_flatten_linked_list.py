class Node(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.down = None # 感觉可以看成左子树

class MergeList(object):
    def __init__(self):
        self.head = None

    # 用来合并两个有序的链表
    def merge(self, a, b):
        # 若其中一个链表为空，直接返回另一个链表
        if a is None:
            return b
        elif b is None:
            return a

        # 把两个链表头中较小的结点赋值给 result
        if a.val < b.val:
            result = a
            result.down = self.merge(a.down, b)
        else:
            result = b
            result.down = self.merge(a, b.down)
        return result

    # 把链表扁平化处理
    def flatten(self, root):
        if root is None or root.right is None:
            return root

        # 递归处理 root.right 链表
        root.right = self.flatten(root.right)

        # 把 root 结点对应的链表与右边的链表合并
        root = self.merge(root, root.right)
        return root

    # 把 val 插入到链表头
    def insert(self, head_ref, val):
        new_node = Node(val)
        new_node.down = head_ref
        head_ref = new_node
        return head_ref

    def printList(self):
        tmp = self.head
        while tmp:
            print(f"{tmp.val:<2}->None")
            print('v')
            tmp = tmp.down
        print("None")

if __name__ == "__main__":
    L = MergeList()

    # 构造链表
    L.head = L.insert(L.head, 31)
    L.head = L.insert(L.head, 8)
    L.head = L.insert(L.head, 6)
    L.head = L.insert(L.head, 3)
    L.head.right = L.insert(L.head.right, 21)
    L.head.right = L.insert(L.head.right, 11)
    L.head.right.right = L.insert(L.head.right.right, 50)
    L.head.right.right = L.insert(L.head.right.right, 22)
    L.head.right.right = L.insert(L.head.right.right, 15)
    L.head.right.right.right = L.insert(L.head.right.right.right, 55)
    L.head.right.right.right = L.insert(L.head.right.right.right, 40)
    L.head.right.right.right = L.insert(L.head.right.right.right, 39)
    L.head.right.right.right = L.insert(L.head.right.right.right, 30)
    """
    搞定后，大致是这样（我用 N 代表 None）
    head: 3 -> 11 -> 15 -> 30 -> N
          v    v     v     v
          6->N 21->N 22->N 39->N
          v    v     v     v
          8->N N     50->N 40->N
          v          v     v
          31->N      N     N
          v
          N
    """

    # 扁平化链表
    L.head = L.flatten(L.head)
    L.printList()

