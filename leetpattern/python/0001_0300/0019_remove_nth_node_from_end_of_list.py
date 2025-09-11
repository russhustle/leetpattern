"""
-   Given the `head` of a linked list, remove the `n-th` node from the end of the list and return its head.
"""

from typing import Optional

from leetpattern.utils import ListNode, list_from_array, list_to_array


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


def test_removeNthFromEnd() -> None:
    head = list_from_array([1, 2, 3, 4, 5])
    assert (list_to_array(removeNthFromEnd(head, 2))) == [1, 2, 3, 5]
