"""
-   Remove all elements from a linked list of integers that have value `val`.

-   Before

```mermaid
graph LR
A((1)) --> B((2))
B --> C((6))
C --> D((3))
D --> E((4))
E --> F((5))
F --> G((6))
G --> H((None))
```

-   After

```mermaid
graph LR
A((1)) --> B((2))
B -.-> C((6))
C -.-> D((3))
D --> E((4))
E --> F((5))
F -.-> G((6))
B --> D((3))
F --> I((None))
```
"""

from typing import Optional

from leetpattern.utils import ListNode


# Iterative
def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    cur = dummy

    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next

    return dummy.next


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |  Iterative  |      O(N)       |    O(1)      |
# |-------------|-----------------|--------------|


nums = [1, 2, 6, 3, 4, 5, 6]
val = 6
head = list_from_array(nums)
print(head)
# 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
print(removeElements(head, val))
# 1 -> 2 -> 3 -> 4 -> 5
