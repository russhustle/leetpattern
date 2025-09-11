"""
-   Remove all nodes from a linked list that have a value greater than `maxValue`.
"""

from typing import Optional

from leetpattern.utils import ListNode, list_from_array, list_to_array


def remove_nodes_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    head.next = remove_nodes_recursive(head.next)

    if head.next and head.val < head.next.val:
        return head.next

    return head


def remove_nodes_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    stack = []
    cur = head

    while cur:
        while stack and cur.val > stack[-1].val:
            stack.pop()

        stack.append(cur)
        cur = cur.next

    dummy = ListNode()
    cur = dummy

    for node in stack:
        cur.next = node
        cur = cur.next

    return dummy.next


def test_remove_nodes() -> None:
    head = list_from_array([5, 2, 13, 3, 8])
    assert (list_to_array(remove_nodes_recursive(head))) == [13, 8]
    head = list_from_array([5, 2, 13, 3, 8])
    assert (list_to_array(remove_nodes_iterative(head))) == [13, 8]
