"""
- Reverse a linked list from position left to position right. Return the linked list after reversing.
"""

from typing import Optional

from leetpattern.utils import ListNode, list_from_array, list_to_array


def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    dummy = ListNode(next=head)
    p0 = dummy
    for _ in range(left - 1):
        if p0.next is None:
            break
        p0 = p0.next

    pre = None
    cur = p0.next
    for _ in range(right - left + 1):
        if not cur:
            break
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt

    if p0.next:
        p0.next.next = cur
    p0.next = pre

    return dummy.next


def test_reverse_between():
    head = list_from_array([1, 2, 3, 4, 5])
    left = 2
    right = 4
    result = reverseBetween(head, left, right)
    assert list_to_array(result) == [1, 4, 3, 2, 5]

    head = list_from_array([5])
    left = 1
    right = 1
    result = reverseBetween(head, left, right)
    assert list_to_array(result) == [5]

    head = list_from_array([3, 5])
    left = 1
    right = 2
    result = reverseBetween(head, left, right)
    assert list_to_array(result) == [5, 3]
