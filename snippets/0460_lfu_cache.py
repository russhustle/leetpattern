from collections import defaultdict


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.freq = 1


class DoubleLinkedList:
    def __init__(self):
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def pop(self) -> Node:
        if self.head.next == self.tail:
            return None
        node = self.tail.prev
        self.remove(node)
        return node

    def is_empty(self) -> bool:
        return self.head.next == self.tail


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_table = {}
        self.freq_table = defaultdict(DoubleLinkedList)
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.key_table:
            return -1
        node = self.key_table[key]
        self._update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_table:
            node = self.key_table[key]
            node.value = value
            self._update(node)
        else:
            if self.size == self.capacity:
                list_to_remove = self.freq_table[self.min_freq]
                node_to_remove = list_to_remove.pop()
                del self.key_table[node_to_remove.key]
                self.size -= 1
            new_node = Node(key, value)
            self.key_table[key] = new_node
            self.freq_table[1].insert(new_node)
            self.min_freq = 1
            self.size += 1

    def _update(self, node: Node):
        freq = node.freq
        self.freq_table[freq].remove(node)
        if self.freq_table[freq].is_empty() and freq == self.min_freq:
            self.min_freq += 1
        node.freq += 1
        self.freq_table[node.freq].insert(node)


obj = LFUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))  # 1
obj.put(3, 3)
print(obj.get(2))  # -1
