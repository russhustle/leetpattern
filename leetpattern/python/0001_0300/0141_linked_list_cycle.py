"""
-   Determine if a linked list has a cycle in it.
"""

from typing import Optional

from leetpattern.utils import ListNode


def hasCycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


print(hasCycle(list_from_array([3, 2, 0, -4])))  # False
print(hasCycle(list_from_array([3, 2, 0, -4], 1)))  # True
