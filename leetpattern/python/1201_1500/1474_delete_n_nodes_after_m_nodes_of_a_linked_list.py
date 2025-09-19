from typing import Optional

from leetpattern.utils import LinkedList, ListNode


def deleteNodes(head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    cur = dummy

    while cur.next:
        for _ in range(m):
            if not cur.next:
                break
            cur = cur.next

        for _ in range(n):
            if not cur.next:
                break
            cur.next = cur.next.next

    return dummy.next


def test_deleteMiddle():
    ll = LinkedList(list(range(1, 14)))
    assert ll.to_array() == list(range(1, 14))

    ll = LinkedList(deleteNodes(ll.head, 2, 3))
    assert ll.to_array() == [1, 2, 6, 7, 11, 12]
