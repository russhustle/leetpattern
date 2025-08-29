---
comments: True
---

# Linked List Others

## Table of Contents

- [x] [138. Copy List with Random Pointer](https://leetcode.cn/problems/copy-list-with-random-pointer/) (Medium)
- [ ] [382. Linked List Random Node](https://leetcode.cn/problems/linked-list-random-node/) (Medium)
- [ ] [430. Flatten a Multilevel Doubly Linked List](https://leetcode.cn/problems/flatten-a-multilevel-doubly-linked-list/) (Medium)
- [ ] [1265. Print Immutable Linked List in Reverse](https://leetcode.cn/problems/print-immutable-linked-list-in-reverse/) (Medium) 👑

## 138. Copy List with Random Pointer

-   [LeetCode](https://leetcode.com/problems/copy-list-with-random-pointer/) | [LeetCode CH](https://leetcode.cn/problems/copy-list-with-random-pointer/) (Medium)

-   Tags: hash table, linked list
```python title="138. Copy List with Random Pointer - Python Solution"
from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head: "Optional[Node]") -> "Optional[Node]":
    if not head:
        return None

    # Copy nodes and link them together
    cur = head
    while cur:
        new_node = Node(cur.val)
        new_node.next = cur.next
        cur.next = new_node
        cur = new_node.next

    # Copy random pointers
    cur = head
    while cur:
        cur.next.random = cur.random.next if cur.random else None
        cur = cur.next.next

    # Separate the original and copied lists
    cur = head
    new_head = head.next
    while cur:
        new_node = cur.next
        cur.next = new_node.next
        new_node.next = new_node.next.next if new_node.next else None
        cur = cur.next

    return new_head

```

## 382. Linked List Random Node

-   [LeetCode](https://leetcode.com/problems/linked-list-random-node/) | [LeetCode CH](https://leetcode.cn/problems/linked-list-random-node/) (Medium)

-   Tags: linked list, math, reservoir sampling, randomized
## 430. Flatten a Multilevel Doubly Linked List

-   [LeetCode](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/) | [LeetCode CH](https://leetcode.cn/problems/flatten-a-multilevel-doubly-linked-list/) (Medium)

-   Tags: linked list, depth first search, doubly linked list
## 1265. Print Immutable Linked List in Reverse

-   [LeetCode](https://leetcode.com/problems/print-immutable-linked-list-in-reverse/) | [LeetCode CH](https://leetcode.cn/problems/print-immutable-linked-list-in-reverse/) (Medium)

-   Tags: linked list, two pointers, stack, recursion
