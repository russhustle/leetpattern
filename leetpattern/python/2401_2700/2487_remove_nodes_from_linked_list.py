from typing import Optional

from leetpattern.utils import LinkedList, ListNode


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
    ll = LinkedList([5, 2, 13, 3, 8])
    ll = LinkedList(remove_nodes_recursive(ll.head))
    assert ll.to_array() == [13, 8]
    ll = LinkedList([5, 2, 13, 3, 8])
    ll = LinkedList(remove_nodes_iterative(ll.head))
    assert ll.to_array() == [13, 8]
