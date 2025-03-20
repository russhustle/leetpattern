---
comments: True
---

# Linked List Applications

## Table of Contents

- [ ] [1019. Next Greater Node In Linked List](https://leetcode.cn/problems/next-greater-node-in-linked-list/) (Medium)
- [x] [1171. Remove Zero Sum Consecutive Nodes from Linked List](https://leetcode.cn/problems/remove-zero-sum-consecutive-nodes-from-linked-list/) (Medium)
- [x] [707. Design Linked List](https://leetcode.cn/problems/design-linked-list/) (Medium)
- [x] [146. LRU Cache](https://leetcode.cn/problems/lru-cache/) (Medium)
- [x] [460. LFU Cache](https://leetcode.cn/problems/lfu-cache/) (Hard)
- [ ] [432. All O`one Data Structure](https://leetcode.cn/problems/all-oone-data-structure/) (Hard)
- [ ] [1206. Design Skiplist](https://leetcode.cn/problems/design-skiplist/) (Hard)

## 1019. Next Greater Node In Linked List

-   [LeetCode](https://leetcode.com/problems/next-greater-node-in-linked-list/) | [LeetCode CH](https://leetcode.cn/problems/next-greater-node-in-linked-list/) (Medium)

-   Tags: array, linked list, stack, monotonic stack

## 1171. Remove Zero Sum Consecutive Nodes from Linked List

-   [LeetCode](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/) | [LeetCode CH](https://leetcode.cn/problems/remove-zero-sum-consecutive-nodes-from-linked-list/) (Medium)

-   Tags: hash table, linked list

```python title="1171. Remove Zero Sum Consecutive Nodes from Linked List - Python Solution"
from typing import Optional

from template import ListNode


# Prefix Sum
def removeZeroSumSublists(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    cur = head
    prefix_sum = 0
    seen = {0: dummy}

    while cur:
        prefix_sum += cur.val
        if prefix_sum in seen:
            node = seen[prefix_sum].next
            temp_sum = prefix_sum
            while node != cur:
                temp_sum += node.val
                del seen[temp_sum]
                node = node.next
            seen[prefix_sum].next = cur.next
        else:
            seen[prefix_sum] = cur
        cur = cur.next

    return dummy.next


head = ListNode().create([1, 2, -3, 3, 1])
print(removeZeroSumSublists(head))  # 3 -> 1

```

## 707. Design Linked List

-   [LeetCode](https://leetcode.com/problems/design-linked-list/) | [LeetCode CH](https://leetcode.cn/problems/design-linked-list/) (Medium)

-   Tags: linked list, design
-   Design your implementation of the linked list. You can choose to use a singly or doubly linked list.

```python title="707. Design Linked List - Python Solution"
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.dummy.next
        for _ in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        self.dummy.next = ListNode(val, self.dummy.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = self.dummy
        while current.next:
            current = current.next
        current.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        current = self.dummy
        for i in range(index):
            current = current.next
        current.next = ListNode(val, current.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        current = self.dummy
        for i in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1


ll = MyLinkedList()
ll.addAtHead(1)
ll.addAtTail(3)
ll.addAtIndex(1, 2)  # 1 -> 2 -> 3
print(ll.get(1))  # 2

```

## 146. LRU Cache

-   [LeetCode](https://leetcode.com/problems/lru-cache/) | [LeetCode CH](https://leetcode.cn/problems/lru-cache/) (Medium)

-   Tags: hash table, linked list, design, doubly linked list
- Design and implement a data structure for **Least Recently Used (LRU) cache**. It should support the following operations: get and put.
- [lru](https://media.geeksforgeeks.org/wp-content/uploads/20240909142802/Working-of-LRU-Cache-copy-2.webp)
- ![146](https://miro.medium.com/v2/resize:fit:650/0*fOwBd3z0XtHh7WN1.png)

| Data structure     | Description                   |
| ------------------ | ----------------------------- |
| Doubly Linked List | To store the key-value pairs. |
| Hash Map           | To store the key-node pairs.  |

```python title="146. LRU Cache - Python Solution"
from collections import OrderedDict


# Doubly Linked List
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
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

    def move_to_last(self, node):
        self.remove(node)
        self.add_to_last(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_last(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.move_to_last(node)
            return None

        if len(self.cache) == self.cap:
            del self.cache[self.head.next.key]
            self.remove(self.head.next)

        node = Node(key=key, val=value)
        self.cache[key] = node
        self.add_to_last(node)


# OrderedDict
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

print("LRU Cache passed")
print("LRU Cache Ordered Dict passed")

```

```cpp title="146. LRU Cache - C++ Solution"
#include <iostream>
#include <unordered_map>
using namespace std;

class Node {
   public:
    int key;
    int val;
    Node *prev;
    Node *next;

    Node(int k = 0, int v = 0) : key(k), val(v), prev(nullptr), next(nullptr) {}
};

class LRUCache {
   private:
    int cap;
    unordered_map<int, Node *> cache;
    Node *head;
    Node *tail;

    void remove(Node *node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    void insert_to_last(Node *node) {
        tail->prev->next = node;
        node->prev = tail->prev;
        tail->prev = node;
        node->next = tail;
    }

    void move_to_last(Node *node) {
        remove(node);
        insert_to_last(node);
    }

   public:
    LRUCache(int capacity) {
        this->cap = capacity;
        head = new Node();
        tail = new Node();
        head->next = tail;
        tail->prev = head;
    }

    int get(int key) {
        if (cache.find(key) != cache.end()) {
            Node *node = cache[key];
            move_to_last(node);
            return node->val;
        }
        return -1;
    }

    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            Node *node = cache[key];
            node->val = value;
            move_to_last(node);
        } else {
            Node *newNode = new Node(key, value);
            cache[key] = newNode;
            insert_to_last(newNode);

            if ((int)cache.size() > cap) {
                Node *removed = head->next;
                remove(removed);
                cache.erase(removed->key);
                delete removed;
            }
        }
    }
};

int main() {
    LRUCache lru(2);
    lru.put(1, 1);
    lru.put(2, 2);
    cout << lru.get(1) << endl;  // 1
    lru.put(3, 3);
    cout << lru.get(2) << endl;  // -1
    lru.put(4, 4);
    cout << lru.get(1) << endl;  // -1
    cout << lru.get(3) << endl;  // 3
    cout << lru.get(4) << endl;  // 4
    return 0;
}

```

## 460. LFU Cache

-   [LeetCode](https://leetcode.com/problems/lfu-cache/) | [LeetCode CH](https://leetcode.cn/problems/lfu-cache/) (Hard)

-   Tags: hash table, linked list, design, doubly linked list

```python title="460. LFU Cache - Python Solution"
from collections import OrderedDict, defaultdict


class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        # key -> [val, freq]
        self.key_to_val_freq = {}
        # freq -> OrderedDict of keys
        self.freq_to_keys = defaultdict(OrderedDict)
        self.min_freq = 0

    def remove_least_frequent(self):

        lfu_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
        del self.key_to_val_freq[lfu_key]

        # If the frequency list is empty after removal, delete it
        if not self.freq_to_keys[self.min_freq]:
            del self.freq_to_keys[self.min_freq]

    def update_freq(self, key):
        """Updates the frequency of an existing key."""
        value, freq = self.key_to_val_freq[key]

        # Remove key from current frequency group
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # Update key frequency
        new_freq = freq + 1
        self.key_to_val_freq[key] = [value, new_freq]
        self.freq_to_keys[new_freq][key] = None

    def add_new_key(self, key, value):
        if len(self.key_to_val_freq) >= self.cap:
            self.remove_least_frequent()

        # Insert the new key with frequency 1
        self.key_to_val_freq[key] = [value, 1]
        self.freq_to_keys[1][key] = None
        self.min_freq = 1

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        self.update_freq(key)
        return self.key_to_val_freq[key][0]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.key_to_val_freq:
            self.key_to_val_freq[key][0] = value
            self.update_freq(key)
        else:
            self.add_new_key(key, value)


lfu = LFUCache(2)
lfu.put(1, 1)
lfu.put(2, 2)
print(lfu.get(1))  # 1
lfu.put(3, 3)
print(lfu.get(2))  # -1
print(lfu.get(3))  # 3
lfu.put(4, 4)
print(lfu.get(1))  # -1
print(lfu.get(3))  # 3

```

## 432. All O`one Data Structure

-   [LeetCode](https://leetcode.com/problems/all-oone-data-structure/) | [LeetCode CH](https://leetcode.cn/problems/all-oone-data-structure/) (Hard)

-   Tags: hash table, linked list, design, doubly linked list

## 1206. Design Skiplist

-   [LeetCode](https://leetcode.com/problems/design-skiplist/) | [LeetCode CH](https://leetcode.cn/problems/design-skiplist/) (Hard)

-   Tags: linked list, design
