# coding:utf-8
# example 11: dict_test.py

import pytest
import random


class Array(object):
    def __init__(self, size=32, init=None):
        self._size = size
        self._items = [init] * size

    def __getitem__(self, idx):
        return self._items[idx]

    def __setitem__(self, idx, val):
        self._items[idx] = val

    def __len__(self):
        return self._size

    def __iter__(self):
        for item in self._items:
            yield item

    def clear(self, val=None):
        for i in range(len(self._items)):
            self._items[i] = val


class Slot(object):
    """
    定义一个 hash 表数组的槽
    一个槽有三种状态
    1. 未使用
    2. 使用过，又空了
    3. 正在用
    """
    def __init__(self, key, val):
        self.key = key
        self.val = val


class HashTable(object):
    UNUSED = None  # slot 未使用
    EMPTY = Slot(None, None)  # 使用过，又空了

    def __init__(self):
        self._table = Array(8, init=HashTable.UNUSED)
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot.key

    def __contains__(self, key):
        idx = self._find_key(key)
        return idx is not None

    @property
    def _load_factor(self):
        # load_factor 超过 0.8 重新分配
        return self.length / len(self._table)

    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    def _find_key(self, key):
        tmp_idx = idx = self._hash(key)
        _len = len(self._table)
        while self._table[idx] is not HashTable.UNUSED:
            if self._table[idx] is HashTable.EMPTY:
                idx = (idx * 5 + 1) % _len  # cpython 的其中一种解决方式
                if tmp_idx == idx:
                    break
                continue
            if self._table[idx].key == key:
                return idx
            else:
                idx = (idx * 5 + 1) % _len  # 按规则找下一个
                if tmp_idx == idx:
                    break
        return None

    def _slot_can_insert(self, idx):
        return (self._table[idx] is HashTable.EMPTY or
                self._table[idx] is HashTable.UNUSED)

    def _find_slot_for_insert(self, key):
        idx = self._hash(key)
        _len = len(self._table)
        while not self._slot_can_insert(idx):
            idx = (idx * 5 + 1) % _len
        return idx

    def _rehash(self):
        old_table = self._table
        newsize = len(self._table) * 2  # 倍增扩容
        self._table = Array(newsize, HashTable.UNUSED)
        self.length = 0

        for slot in old_table:
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                idx = self._find_slot_for_insert(slot.key)
                self._table[idx] = slot
                self.length += 1

    def add(self, key, val):
        idx = self._find_key(key)
        if idx is None:
            idx = self._find_slot_for_insert(key)
            self._table[idx] = Slot(key, val)
            self.length += 1
            if self._load_factor >= 0.8:
                self._rehash()
            return True
        else:
            self._table[idx].val = val
            return False

    def get(self, key, default=None):
        idx = self._find_key(key)
        return default if idx is None else self._table[idx].val

    def remove(self, key):
        idx = self._find_key(key)
        if idx is None:
            raise KeyError()
        val = self._table[idx].val
        self.length -= 1
        self._table[idx] = HashTable.EMPTY
        return val


# 上面是 HashTable 的代码，下边是 Dict 的实现
class DictADT(HashTable):
    def __setitem__(self, key, val):
        self.add(key, val)

    def __getitem__(self, key):
        if key not in self:
            raise KeyError()
        else:
            return self.get(key)

    def _iter_slot(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot

    def items(self):
        for slot in self._iter_slot():
            yield (slot.key, slot.val)

    def keys(self):
        for slot in self._iter_slot():
            yield slot.key

    def values(self):
        for slot in self._iter_slot():
            yield slot.val


# use pytest
d = DictADT()
size = 30
seq = list(range(size))


class TestDictADT(object):

    def test_add(self):
        d['a'] = 97
        assert d['a'] == 97
    
    def test_remove(self):
        d.remove('a')
        assert d.get('a') == None

    def test_rehash(self):
        random.shuffle(seq)
        for i in seq:
            d.add(i, i)
        for i in range(size):
            assert d.get(i) == i

    def test_keys(self):
        assert sorted(list(d.keys())) == sorted(seq)

    def test_values(self):
        assert sorted(list(d.values())) == sorted(seq)
