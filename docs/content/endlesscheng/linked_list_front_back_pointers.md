---
comments: True
---

# Linked List Front Back Pointers

## Table of Contents

- [x] [19. Remove Nth Node From End of List](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/) (Medium)
- [ ] [61. Rotate List](https://leetcode.cn/problems/rotate-list/) (Medium)
- [ ] [1721. Swapping Nodes in a Linked List](https://leetcode.cn/problems/swapping-nodes-in-a-linked-list/) (Medium)
- [x] [1474. Delete N Nodes After M Nodes of a Linked List](https://leetcode.cn/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/) (Easy) 👑

## 19. Remove Nth Node From End of List

-   [LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [LeetCode CH](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/) (Medium)

-   Tags: linked list, two pointers
-   Given the `head` of a linked list, remove the `n-th` node from the end of the list and return its head.

```python title="19. Remove Nth Node From End of List - Python Solution"
from typing import Optional

from template import ListNode


# Linked List
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    fast, slow = dummy, dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next


head = [1, 2, 3, 4, 5]
n = 2
head = ListNode.create(head)
print(head)  # 1 -> 2 -> 3 -> 4 -> 5
print(removeNthFromEnd(head, n))  # 1 -> 2 -> 3 -> 5

```

## 61. Rotate List

-   [LeetCode](https://leetcode.com/problems/rotate-list/) | [LeetCode CH](https://leetcode.cn/problems/rotate-list/) (Medium)

-   Tags: linked list, two pointers
## 1721. Swapping Nodes in a Linked List

-   [LeetCode](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/) | [LeetCode CH](https://leetcode.cn/problems/swapping-nodes-in-a-linked-list/) (Medium)

-   Tags: linked list, two pointers
## 1474. Delete N Nodes After M Nodes of a Linked List

-   [LeetCode](https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/) | [LeetCode CH](https://leetcode.cn/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/) (Easy)

-   Tags: linked list
```python title="1474. Delete N Nodes After M Nodes of a Linked List - Python Solution"
from typing import Optional

from template import ListNode


# Linked List
def deleteNodes(
    head: Optional[ListNode], m: int, n: int
) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    cur = dummy

    while cur.next:
        for _ in range(m):
            if not cur.next:
                break
            cur = cur.next

        for _ in range(n):
            if not cur.next:
                break
            cur.next = cur.next.next

    return dummy.next


if __name__ == "__main__":
    head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    m = 2
    n = 3
    head = ListNode.create(head)
    print(head)
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13
    head = deleteNodes(head, m, n)
    print(head)
    # 1 -> 2 -> 6 -> 7 -> 11 -> 12

```

