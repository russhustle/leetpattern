"""
-   Given a number represented as a linked list, double it and return the resulting linked list.
"""

from typing import Optional

from leetpattern.utils import ListNode, list_from_array, list_to_array


def doubleIt(head: Optional[ListNode]) -> Optional[ListNode]:

    def twice(node):
        if not node:
            return 0
        doubled_value = node.val * 2 + twice(node.next)
        node.val = doubled_value % 10
        return doubled_value // 10

    carry = twice(head)

    if carry:
        head = ListNode(val=carry, next=head)

    return head


def test_doubleIt() -> None:
    head = list_from_array([9, 9, 9])
    assert (list_to_array(doubleIt(head))) == [1, 9, 9, 8]
