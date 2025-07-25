"""
-   Given a linked list, return the node where the cycle begins. If there is no cycle, return `None`.

```mermaid
graph LR
A[3] --> B[2]
B --> C[0]
C --> D[-4]
D --> B
```
"""

from typing import Optional

from template import ListNode


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow

    return None


head1 = ListNode.create([3, 2, 0, -4], 1)
print(detectCycle(head1).val)  # 2
head2 = ListNode.create([3, 2, 0, -4])
print(detectCycle(head2))  # None
