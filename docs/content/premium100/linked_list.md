---
comments: True
---

# Linked List

## Table of Contents

- [x] [1474. Delete N Nodes After M Nodes of a Linked List](https://leetcode.cn/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/) (Easy) 👑
- [ ] [708. Insert into a Sorted Circular Linked List](https://leetcode.cn/problems/insert-into-a-sorted-circular-linked-list/) (Medium) 👑
- [ ] [369. Plus One Linked List](https://leetcode.cn/problems/plus-one-linked-list/) (Medium) 👑
- [ ] [1265. Print Immutable Linked List in Reverse](https://leetcode.cn/problems/print-immutable-linked-list-in-reverse/) (Medium) 👑

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

## 708. Insert into a Sorted Circular Linked List

-   [LeetCode](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/) | [LeetCode CH](https://leetcode.cn/problems/insert-into-a-sorted-circular-linked-list/) (Medium)

-   Tags: linked list
## 369. Plus One Linked List

-   [LeetCode](https://leetcode.com/problems/plus-one-linked-list/) | [LeetCode CH](https://leetcode.cn/problems/plus-one-linked-list/) (Medium)

-   Tags: linked list, math
## 1265. Print Immutable Linked List in Reverse

-   [LeetCode](https://leetcode.com/problems/print-immutable-linked-list-in-reverse/) | [LeetCode CH](https://leetcode.cn/problems/print-immutable-linked-list-in-reverse/) (Medium)

-   Tags: linked list, two pointers, stack, recursion
