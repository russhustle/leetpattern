"""
-   Represent the sum of two numbers as a linked list.
"""

from typing import Optional

from leetpattern.utils import LinkedList, ListNode


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    carry = 0

    while l1 or l2:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        carry, val = divmod(v1 + v2 + carry, 10)
        cur.next = ListNode(val)
        cur = cur.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry:
        cur.next = ListNode(val=carry)

    return dummy.next


def test_add_two_numbers():
    l1 = LinkedList([2, 4, 3]).head
    l2 = LinkedList([5, 6, 4]).head
    added = add_two_numbers(l1, l2)
    assert LinkedList(added).to_array() == [7, 0, 8]
