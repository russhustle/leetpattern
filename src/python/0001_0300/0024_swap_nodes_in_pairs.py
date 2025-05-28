"""
-   Given a linked list, swap every two adjacent nodes and return its head.
"""

from typing import Optional

from template import ListNode


# Linked List
def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    n0 = dummy
    n1 = dummy.next

    while n1 and n1.next:
        n2 = n1.next
        n3 = n2.next

        n0.next = n2
        n2.next = n1
        n1.next = n3

        n0 = n1
        n1 = n3

    return dummy.next


nums = [1, 2, 3, 4, 5]
head = ListNode.create(nums)
print(head)
# 1 -> 2 -> 3 -> 4 -> 5
print(swapPairs(head))
# 2 -> 1 -> 4 -> 3 -> 5
