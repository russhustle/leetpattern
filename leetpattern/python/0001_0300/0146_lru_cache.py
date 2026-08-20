from collections import OrderedDict


class DoublyListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    """
    Design and implement a data structure for Least Recently Used (LRU) cache.
    It should support the following operations: get and put.
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = DoublyListNode()
        self.tail = DoublyListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_last(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add_to_last(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add_to_last(node)
        else:
            node = DoublyListNode(key=key, val=value)
            self.cache[key] = node
            self.add_to_last(node)

        if len(self.cache) > self.cap:
            lru = self.head.next
            del self.cache[lru.key]
            self.remove(lru)


class LRUCacheOrderedDict:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key, last=True)
        return self.cache[key]

    def put(self, key: int, value: int):
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
        elif len(self.cache) >= self.cap:
            self.cache.popitem(last=False)

        self.cache[key] = value


def test_lru_cache():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    updated = LRUCache(2)
    updated.put(1, 1)
    updated.put(2, 2)
    updated.put(1, 10)
    updated.put(3, 3)
    assert updated.get(1) == 10
    assert updated.get(2) == -1

    single = LRUCache(1)
    single.put(1, 1)
    single.put(2, 2)
    assert single.get(1) == -1
    assert single.get(2) == 2


def test_lru_cache_ordered_dict():
    cache = LRUCacheOrderedDict(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
