# coding:utf-8
# example 20: bst.py


class BSTNode(object):
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class BST(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        cls.size = 0
        key_to_node_dict = {}
        # [{'key': 60, 'left': 12, 'right': 90, 'is_root': True},...]
        for node_dict in node_list:
            key = node_dict['key']
            key_to_node_dict[key] = BSTNode(key, val=key)  # key, val 暂且同值

        for node_dict in node_list:
            key = node_dict['key']
            node = key_to_node_dict[key]
            if node_dict['is_root']:
                root = node
            node.left = key_to_node_dict.get(node_dict['left'])
            node.right = key_to_node_dict.get(node_dict['right'])
            cls.size += 1
        return cls(root)  # BST(root)

    def _bst_search(self, subtree, key):
        if subtree is None:  # 没找到
            return None
        elif key < subtree.key:
            return self._bst_search(subtree.left, key)
        elif subtree.key < key:
            return self._bst_search(subtree.right, key)
        else:
            return subtree

    def __contains__(self, key):
        return self._bst_search(self.root, key) is not None

    def get(self, key, default=None):
        node = self._bst_search(self.root, key)
        return node.val if node else default

    def _bst_min_node(self, subtree):  # 找左下角
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._bst_min_node(subtree.left)

    def bst_min(self):
        node = self._bst_min_node(self.root)
        return node.val if node else None

    def _bst_insert(self, subtree, key, val):
        """插入并且返回根结点"""
        if subtree is None:  # 插入的结点一定是根结点，包括 root 为空的情况
            subtree = BSTNode(key, val)
        elif key < subtree.key:
            subtree.left = self._bst_insert(subtree.left, key, val)
        elif subtree.key < key:
            subtree.right = self._bst_insert(subtree.right, key, val)
        return subtree

    def add(self, key, val):
        node = self._bst_search(self.root, key)
        if node is None:
            self.root = self._bst_insert(self.root, key, val)
            self.size += 1
            return True
        else:  # 更新
            node.val = val
            return False

    def _bst_remove(self, subtree, key):
        """删除并返回根结点"""
        if subtree is None:
            return None
        elif key < subtree.key:
            subtree.left = self._bst_remove(subtree.left, key)
            return subtree
        elif key > subtree.key:
            subtree.right = self._bst_remove(subtree.right, key)
            return subtree
        else:  # 找到了需要删除的结点
            if subtree.left is None and subtree.right is None:  # 叶子结点
                return None
            elif subtree.left is None or subtree.right is None:  # 只有一个孩子
                if subtree.left is not None:
                    return subtree.left  # 返回它的孩子并让它的父亲指过去
                else:
                    return subtree.right
            else:  # 俩孩子，寻找后继结点替换，并删除该后继结点（更新其右子树）
                successor_node = self._bst_min_node(subtree.right)
                subtree.key = successor_node.key
                subtree.val = successor_node.val
                subtree.right = self._bst_remove(subtree.right,
                                                 successor_node.key)
                return subtree

    def remove(self, key):
        assert key in self
        self.size -= 1
        return self._bst_remove(self.root, key)


#                60
#           /          \
#          12           90
#        /    \        /  \
#       4      41    71    100
#      / \    / \   / \    / \
#     1   N  29  N N  84  N   N
#    / \    / \
#  23   37 N   N
#  /\   /\
# N  N N  N
NODE_LIST = [
    {'key': 60, 'left': 12, 'right': 90, 'is_root': True},
    {'key': 12, 'left': 4, 'right': 41, 'is_root': False},
    {'key': 4, 'left': 1, 'right': None, 'is_root': False},
    {'key': 1, 'left': None, 'right': None, 'is_root': False},
    {'key': 41, 'left': 29, 'right': None, 'is_root': False},
    {'key': 29, 'left': 23, 'right': 37, 'is_root': False},
    {'key': 23, 'left': None, 'right': None, 'is_root': False},
    {'key': 37, 'left': None, 'right': None, 'is_root': False},
    {'key': 90, 'left': 71, 'right': 100, 'is_root': False},
    {'key': 71, 'left': None, 'right': 84, 'is_root': False},
    {'key': 100, 'left': None, 'right': None, 'is_root': False},
    {'key': 84, 'left': None, 'right': None, 'is_root': False},
]


# use pytest
bst = BST.build_from(NODE_LIST)


class TestBSTTree(object):

    def test_init(self):
        for node_dict in NODE_LIST:
            key = node_dict['key']
            assert bst.get(key) == key
        assert bst.get(-1) is None
        assert bst.size == len(NODE_LIST)

    def test_min(self):
        assert bst.bst_min() == 1

    def test_add(self):
        bst.add(0, 0)
        assert bst.bst_min() == 0

    def test_remove(self):
        bst.remove(12)
        assert bst.get(12) is None

        bst.remove(1)
        assert bst.get(1) is None

        bst.remove(29)
        assert bst.get(29) is None
