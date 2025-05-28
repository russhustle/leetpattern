"""
-   Determine if a linked list has a cycle in it.

```mermaid
graph LR
    A((3)) --> B((2))
    B --> C((0))
    C --> D((4))
```

```mermaid
graph LR
    A((3)) --> B((2))
    B --> C((0))
    C --> D((4))
    D --> B
```
"""

from typing import Optional

from template import ListNode


def hasCycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


print(hasCycle(ListNode.create([3, 2, 0, -4])))  # False
print(hasCycle(ListNode.create([3, 2, 0, -4], 1)))  # True
