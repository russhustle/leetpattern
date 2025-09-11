"""
-   Given a linked list, swap every two adjacent nodes and return its head.
"""

from typing import Optional

from leetpattern.utils import ListNode, list_from_array, list_to_array


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
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


def test_swap_pairs():
    head = list_from_array([1, 2, 3, 4, 5])
    assert list_to_array(swap_pairs(head)) == [2, 1, 4, 3, 5]
